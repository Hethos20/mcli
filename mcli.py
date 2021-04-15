#!/usr/bin/env python3
import os

homedir = (os.path.expanduser('~'))
mpddir = '.mpd'
ncmpcppdir = '.ncmpcpp'

creatempd = os.path.join(homedir, mpddir)
createncmpcpp = os.path.join(homedir, ncmpcppdir)
os.mkdir(creatempd)
os.mkdir(createncmpcpp)

ncmpcpp_config = open('default_config', 'r')
ncmpcpp_content = ncmpcpp_config.read().splitlines()

music_dir = input("Enter the absolute path of your music directory\n")
userName = input("Enter your user name\n")

ncmpcpp_content[1] = '''mpd_music_dir = "'''+music_dir+'''"'''
ncmpcpp_content[4] = '''visualizer_output_name = "'''+userName+'''"'''
ncmpcpp_config.close()

ncmpcpp_final = open(createncmpcpp+'\config','x')

for i in ncmpcpp_content:
    ncmpcpp_final.write(i+"\n")
ncmpcpp_final.close()

mpd_config = open('default_mpd.conf', 'r')
mpd_content = mpd_config.read().splitlines()

mpd_content[0] = '''music_directory "'''+music_dir+'''"'''
mpd_content[1] = '''playlist_directory"'''+music_dir+'''"'''
mpd_content[12] = '''    name                    "'''+userName+'''"'''
mpd_config.close()

mpd_final = open(creatempd+'\mpd.conf', 'x')

for i in mpd_content:
    mpd_final.write(i+"\n")
mpd_final.close()



