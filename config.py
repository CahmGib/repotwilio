#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3635a0dc-fc77-4b50-a491-63b8d083c99d")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "QMX8Q~s1qpd-o1AvDwUxep6aT4ob11mEMZXDvbRN")
    ACCOUNT_SID = os.environ.get("sid","ACbcfc25858d83ab1b477529564d4d4114")
    AUTH_TOKEN = os.environ.get("auth_token","933bf694c22ba731740c77b9cca9c7a1")
    PHONE_NUMER = os.environ.get("phone_number","whatsapp:+120770768346")
    
