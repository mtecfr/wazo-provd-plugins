# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

common = {}
execfile_('common.py', common)


MODEL_VERSIONS = {
    u'N870 IP PRO': u'83.V2.39.0',
}


class GigasetPlugin(common['BaseGigasetPlugin']):
    IS_PLUGIN = True

    pg_associator = common['BaseGigasetPgAssociator'](MODEL_VERSIONS)
