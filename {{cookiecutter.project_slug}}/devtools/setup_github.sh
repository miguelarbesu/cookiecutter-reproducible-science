#!/usr/bin/env bash
# -*- coding: utf-8 -*-

dpkg -s gh &> /dev/null  

if [ $? -ne 0 ]

    then
        echo "GitHub CLI not installed"
    else
        echo "Creating GitHub repository..."
        gh repo create {{ cookiecutter.project_slug}}
        git push --set-upstream origin main
fi
