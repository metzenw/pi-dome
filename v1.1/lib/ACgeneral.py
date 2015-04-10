#!/usr/bin/env python
# ====================================================================
# support-dig script that gathers diagnostics for Adaptive Computing 
# support. 
#
# Copyright (C) 2005-2015 by Adaptive Computing Enterprises, Inc. 
# All Rights Reserved.
#
# THIS SOFTWARE SCRIPT IS PROVIDED BY ADAPTIVE COMPUTING ENTERPRISES, 
# INC. "AS IS" AND IS FOR REFERENCE USE ONLY.  ANY EXPRESS OR IMPLIED 
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL ADAPTIVE COMPUTING ENTERPRISES, INC. 
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
# OR CONSEQUENTIAL DAMAGES ARISING FROM THE USE THEREOF.
# ====================================================================

# ====================================================================
# Import from libraries and validate Python version
# ====================================================================

# Import Libraries
import re
import subprocess
import shutil
import glob
import threading
import time
import datetime
import tarfile

# ====================================================================
# Walk the os directory and find file dates and mtime
# ====================================================================
def return_file_and_mtime(dir_to_crawl):
    """

    :param dir_to_crawl:
    :return:
    """
    files_and_dates = {}
    for root, dirs, files in os.walk(dir_to_crawl):
        for name in files:
            file_time = time.gmtime(modification_date(os.path.join(root, name)))
            dt = datetime.datetime.fromtimestamp(time.mktime(file_time))
            files_and_dates[name] = format_iso_date(dt)
    return files_and_dates

# ====================================================================
# Format date to yyyymmdd from datetime.now() e.g format yyyy-mm-dd
# ====================================================================
def format_iso_date(date_to_format):
    """

    :param date_to_format:
    :return:
    """
    log_date_format_today = str(datetime.date(date_to_format.year, date_to_format.month, date_to_format.day))
    log_date_format_today = log_date_format_today.replace("-", "")
    return log_date_format_today

# ====================================================================
# Function to copy pattern in file names with glob.iglob
# ====================================================================
def cp_file_pattern(logs_to_copy, output_directory):
    """

    :param logs_to_copy:
    :param output_directory:
    :return:
    """
    for file_name in glob.iglob(logs_to_copy):
        try:
            shutil.copy2(file_name, output_directory)
        except IOError, e:
            print "Unable to copy " + str(file_name) + str(e)
    return 0

# ====================================================================
# Gather os modified time from a file *Called by return_file_and_mtime 
# ====================================================================
def modification_date(filename):
    """

    :param filename:
    :return:
    """
    t = os.path.getmtime(filename)
    return t

# ====================================================================
# Gather os created time /Not used/ *Called by return_file_and_mtime()
# ====================================================================
def creation_date(filename):
    """

    :param filename:
    :return:
    """
    t = os.path.getctime(filename)
    return t

# ====================================================================
# This will tar and gzip the data
# ====================================================================
def bundle_package(output_filename, source_dir, tmp_directory):
    """

    :param output_filename:
    :param source_dir:
    :param tmp_directory:
    :return:
    """
    os.chdir(tmp_directory)
    tar_name = output_filename + ".tar.gz"
    print "Compressing: " + tar_name + " into " + tmp_directory
    #Tar the diagnostics
    tar = tarfile.open(tar_name, "w:gz")
    tar.add(source_dir, arcname=output_filename)
    return 0

# ====================================================================
# SCP/FTP the files to Adaptive Computing
# ====================================================================
def transfer_package(output_filename, tmp_directory):
    """

    :param output_filename:
    :param tmp_directory:
    :return:
    """
    tar_name = output_filename + ".tar.gz"
    if use_ssh:
        print "I will now ssh the file to Adaptive. \n"
        print "*********************************************"
        print "When prompted for a password enter \"hello\""
        print "********************************************* \n"
        os.system("scp "+tmp_directory+output_filename+".tar.gz guest@ssh.adaptivecomputing.com:/home/guest/")
        print "SCP has completed for " + tar_name
    if use_ftp:
        ftp_file_name = tmp_directory+output_filename + ".tar.gz"
        print "I will now ftp the file to Adaptive."
        import ftplib
        session = ftplib.FTP('ftp.adaptivecomputing.com', 'moabguest', 'moabpassword')
        diag_file = open(ftp_file_name, 'rb')            # file to send
        session.storbinary('STOR '+tar_name, diag_file)  # send the file
        diag_file.close()                                # close file and FTP
        session.quit()
        print "FTP has completed for " + tar_name
    return 0

# ====================================================================
# This function runs a command and saves the command title and output
# e.g mdiag -a - > mdiag_-a.txt and the output from the command is
# written to the file.
# run_and_save("mdiag -n -v", "mdiag_n_v.txt")
# ====================================================================
def run_and_save(command_to_run, output_file, output_directory):
    """

    :param command_to_run:
    :param output_file:
    :param output_directory:
    :return:
    """
    sys.path.append(moab_object["moab_bin_path"])
    sys.path.append(moab_object["moab_sbin_path"])
    os.chdir(output_directory)
    p = subprocess.Popen(command_to_run, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if len(error) > 0:
        print "Command %s failed" % command_to_run + " " + error
        return 1
    f_handler = open(output_directory+output_file, "w+")
    f_handler.write(str(output))
    f_handler.close()
    return 0

# ====================================================================
# This function saves data to a file from a variable
# ====================================================================
def save_output(output, output_file, output_directory):
    os.chdir(output_directory)
    f_handler = open(output_directory+output_file, "w+")
    f_handler.write(str(output))
    f_handler.close()
    return 0

# ====================================================================
# This runs a command and does not worry about output/success 
# ====================================================================
def exec_cmd(command_to_run):
    """

    :param command_to_run:
    :return:
    """
    p = subprocess.Popen(command_to_run, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return 0


# ====================================================================
# Run a command and return its output
# ====================================================================
def run_and_return_output(command_to_run):
    """

    :param command_to_run:
    :return:
    """
    p = subprocess.Popen(command_to_run, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if len(error) > 0:
        return 1, error
    else:
        return 0, output

# ====================================================================
# This will replace "def which". Used to determin if bin is in path.
# ====================================================================
def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# ====================================================================
# Clean up directories
# ====================================================================
def clean_up(output_directory):
    """

    :param output_directory:
    :return:
    """
    print "Remove tmp output dir? : " + output_directory
    while True:
        remove_answer = str(raw_input("Enter (Y/N) :"))
        remove_answer = remove_answer.upper()
        if remove_answer == "Y":
            print("Removing tmp dir: " + output_directory)
            shutil.rmtree(output_directory)
            return 0
        if remove_answer == "N":
            return 0

# ====================================================================
# Function to find value between two delimiters e.g. "1234" 1,4 = 23
# ====================================================================
def find_between(s, first, last):
    """

    :param s:
    :param first:
    :param last:
    :return:
    """
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


