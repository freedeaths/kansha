#--
# Copyright (c) 2012-2014 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
#--

from nagare.services import plugin

from kansha.events import EventHandlerMixIn


class CardExtension(plugin.Plugin, EventHandlerMixIn):
    CATEGORY = 'card-extension'

    def __init__(self, card, action_log, configurator=None):
        self.card = card
        self.action_log = action_log
        self.configurator = configurator

    @staticmethod
    def get_excel_title():
        '''If the extension is exportable in Excel, return its column name'''
        return None

    def write_excel_sheet(self, sheet, row, col, style):
        '''Write value in Excel sheet'''
        pass

    @staticmethod
    def get_schema_def():
        '''If the extension has to be indexed for it to be used in search engine, return some schema field
        ie: return schema.TEXT for a text field'''
        return None

    def to_document(self):
        '''How to transform extension value for it to be indexed'''
        return None

    def delete(self):
        '''Happens when a card is deleted, use it to clean up files for example'''
        pass

    def copy(self, parent, additional_data):
        '''Happens when a card is copied'''
        return self.__class__(parent, parent.action_log)

    def new_card_position(self, value):
        '''Happens when a card is moved on the board'''
        pass
