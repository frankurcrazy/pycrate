# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/si6_rest_octets.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.35a SI 6 Rest Octets
# top-level object: SI6 rest octets



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

paging_channel_restructuring = CSN1Alt(name='paging_channel_restructuring', alt={
  '0': ('', []),
  '1': ('', [])})

pch_and_nch_info = CSN1List(name='pch_and_nch_info', list=[
  CSN1Ref(obj=paging_channel_restructuring),
  CSN1Bit(name='nln_sacch', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='call_priority', bit=3)])}),
  CSN1Bit(name='nln_status_sacch')])

band_indicator = CSN1Alt(name='band_indicator', alt={
  'H': ('', []),
  'L': ('', [])})

si6_rest_octets = CSN1List(name='si6_rest_octets', list=[
  CSN1Alt(alt={
    'H': ('', [
    CSN1Ref(obj=pch_and_nch_info)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='vbs_vgcs_options', bit=2)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('dtm_support', [
    CSN1Bit(name='rac', bit=8),
    CSN1Bit(name='max_lapdm', bit=3)]),
    'L': ('dtm_support', [])}),
  CSN1Ref(obj=band_indicator),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='gprs_ms_txpwr_max_cch', bit=5)]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='dedicated_mode_mbms_notification_support'),
    CSN1Bit(name='mnci_support')]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='amr_config', bit=4)])})]),
    'L': ('', [])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Bit(name='random_bit_stream', bit=-1)]),
    'L': ('', [])}),
  CSN1Ref(obj=spare_padding)])

inband_pagings = CSN1Alt(name='inband_pagings', alt={
  '0': ('', []),
  '1': ('', [])})

inband_notifications = CSN1Alt(name='inband_notifications', alt={
  '0': ('', []),
  '1': ('', [])})

vbs_vgcs_options = CSN1List(name='vbs_vgcs_options', list=[
  CSN1Ref(obj=inband_notifications),
  CSN1Ref(obj=inband_pagings)])

