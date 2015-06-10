#// clsCampaign.py - The Campaign class encapsulates all data for a specific campaign.

#//---------------------------------------------------------------------------------
#//-----------------------------Module Packages to be imported----------------------
#//---------------------------------------------------------------------------------
import ui, os
import console
import xml.etree.ElementTree as xmlElementTree

#//---------------------------------------------------------------------------------
#//-----------------------------Class Definitions-----------------------------------
#//---------------------------------------------------------------------------------
class clsCampaign:
  """
  _Attributes:
  Methods:
  Exceptions:
  """

  def __init__(self, strName = '', strDescription = '', strReferee = '', dteStartDate = '', strSetting = '', lstCampaignLog = [], lstAssetStore = [], strCampaignNotes ='', blnActiveCampaign = True):
    """
    The class initialise function
    Arguments:
    Specifics:
    """

    try:
      self.Name = strName
      self.Description = strDescription
      self.Referee = strReferee
      self.StartDate = dteStartDate
      self.Setting = strSetting
      self.CampaignLog = lstCampaignLog
      #print(self.CampaignLog)
      self.AssetStore = lstAssetStore
      self.CampaignNotes = strCampaignNotes
      self.ActiveCampaign = blnActiveCampaign
      self.IsDirty = False 

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Attribute Defintions--------------------------------
  def set_name(self, NewValue):
    """
    To set attribute name for the campaign
    Arguments:
    NewValue: The new value which the attribute will be set to.
    Specifics:
    """

    try:
      self.Name = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_name(self):
    """
    To get attribute name for the campaign
    Arguments:
    Specifics:
    """

    try:
      return self.Name

    except:
      pass

  def set_description(self, NewValue):
    """
    To set attribute description for the campaign
    Arguments:
    NewValue: The new value which the attribute will be set to.
    Specifics:
    """

    try:
      self.Description = NewValue
      self.IsDirty = True 
    except:
      pass

  def get_description(self):
    """
    To get attribute description for the campaign
    Arguments:
    Specifics:
    """

    try:
      return self.Description

    except:
      pass

  def set_referee(self, NewValue):
    """
    To set the referee acting for the campaign
    Arguments:
    NewValue: The new value which the attribute will be set to.
    Specifics:
    """

    try:
      self.Referee = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_referee(self):
    """
    To get the referee acting for the campaign
    Arguments:
    Specifics:
    """

    try:
      return self.Referee

    except:
      pass

  def set_start_date(self, NewValue):
    """
    To set attribute real world start date for the campaign
    Arguments:
    NewValue: The new value which the attribute will be set to.
    Specifics:
    """

    try:
      self.StartDate = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_start_date(self):
    """
    To get attribute real world start date for the campaign
    Arguments:
    Specifics:
    """

    try:
      return self.StartDate

    except:
      pass

  def set_setting(self, NewValue):
    """
    To set attribute for the setting the campaign will be in e.g. New Era, Third Imperium, etc.
    Arguments:
    NewValue: The new value which the attribute will be set to.
    Specifics:
    """

    try:
      self.Setting = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_setting(self):
    """
    To get attribute for the setting the campaign will be in e.g. New Era, Third Imperium, etc.
    Arguments:
    Specifics:
    """

    try:
      return self.Setting

    except:
      pass

  def set_campaign_log(self, NewValue):
    """
    To set the log for the campaign
    Arguments:
    NewValue: The new value which is a list of list of log entries where each entry is a list of
              [gamedate, playerinfo, refereeinfo]
    Specifics:
    """

    try:
      self.CampaignLog = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_campaign_log(self):
    """
    To get the log for the campaign
    Arguments:
    Specifics: returns a list of lists of log entries where each entry is a list of
              [gamedate, playerinfo, refereeinfo]
    """

    try:
      #print('in get campaign log')
      return self.CampaignLog

    except:
      pass

  def set_asset_store(self, NewValue):
    """
    To set the asset store for the campaign
    Arguments:
    NewValue: The new value which is a list of assets for the campaign where each entry is a list of
              [assetname, assetdescription]
    Specifics:
    """

    try:
      self.AssetStore = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_asset_store(self):
    """
    To get the asset store for the campaign
    Arguments:
    Specifics: returns a list of assets for the campaign where each entry is a list of
              [assetname, assetdescription]
    """

    try:
      #print('in get campaign assets')
      return self.AssetStore

    except:
      pass

  def set_campaign_notes(self, NewValue):
    """
    To set the campaign notes for the campaign
    Arguments:
    NewValue: 
    Specifics:
    """

    try:
      self.CampaignNotes = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_campaign_notes(self):
    """
    To get the campaign notes for the campaign
    Arguments:
    Specifics: 
    """

    try:
      #print('in get campaign assets')
      return self.CampaignNotes

    except:
      pass

  def set_active_campaign(self, NewValue):
    """
    To set the campaign notes for the campaign
    Arguments:
    NewValue: 
    Specifics:
    """

    try:
      self.ActiveCampaign = NewValue
      self.IsDirty = True 

    except:
      pass

  def get_active_campaign(self):
    """
    To get the campaign notes for the campaign
    Arguments:
    Specifics: 
    """

    try:
      #print('in get campaign assets')
      return self.ActiveCampaign

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Method Defintions-----------------------------------

  def append_campaign_log_entry(self, dteEntryDate, strPlayerInfo, strRefInfo):
    """
    Adds a fresh log entry at the end of the log list
    Arguments:
    Specifics:
    """
    try:
      #print('In append_campaign_log_entry')
      lstEntry = [dteEntryDate, strPlayerInfo, strRefInfo]
      self.CampaignLog.append(lstEntry)

    except:
      pass

  def save(self, SourceDest = 'xml', CampaignDataDirectory = '/Data/Campaigns/'):
    """
    Adds a fresh log entry at the end of the log list
    Arguments:
    Specifics:
    """
    try:
      #print('in save', CampaignDataDirectory)
      if SourceDest == 'xml':
        self._save_xml(CampaignDataDirectory)
      else:
        pass

    except:
      pass

  def load(self, strFileName, SourceDest = 'xml'):
    """
    Adds a fresh log entry at the end of the log list
    Arguments:
    Specifics:
    """
    try:
      #print('in save')
      if SourceDest == 'xml':
        self._load_xml(strFileName)
      else:
        pass

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Internal Method Defintions--------------------------
  def _save_xml(self, CampaignDataDirectory):
    """
      saves the campaign attributes into an xml file. 
    Arguments:
    Specifics:
    """
    try:
      #print('in _save_xml')
      strFileName = os.getcwdu() + CampaignDataDirectory + self.Name +'.xml'
      #print(strFileName)

      
      if self.ActiveCampaign:
        xmlCampaign = xmlElementTree.Element('TravellerCampaign', name = self.Name, active = 'True')
      else:
        xmlCampaign = xmlElementTree.Element('TravellerCampaign', name = self.Name, active = 'False')
      
      xmlDescription = xmlElementTree.SubElement(xmlCampaign, 'Description').text = self.Description
      xmlReferee = xmlElementTree.SubElement(xmlCampaign, 'Referee').text = self.Referee
      xmlStartDate = xmlElementTree.SubElement(xmlCampaign, 'StartDate').text = self.StartDate
      xmlSetting = xmlElementTree.SubElement(xmlCampaign, 'Setting').text = self.Setting
      xmlLog = xmlElementTree.SubElement(xmlCampaign, 'Log')
      for Entry in self.CampaignLog:
        xmlLogEntry = xmlElementTree.SubElement(xmlLog, 'LogEntry', EntryDate = Entry[0])
        xmlElementTree.SubElement(xmlLogEntry, 'LogEntryPlayer').text = Entry[1]
        xmlElementTree.SubElement(xmlLogEntry, 'LogEntryReferee').text = Entry[2]
      
      xmlAssets = xmlElementTree.SubElement(xmlCampaign, 'Assets')
      for Asset in self.AssetStore:
        xmlAsset = xmlElementTree.SubElement(xmlAssets, 'Asset')
        xmlElementTree.SubElement(xmlAsset, 'AssetName').text = Asset[0]
        xmlElementTree.SubElement(xmlAsset, 'AssetDescription').text = Asset[1]
      
      xmlNotes = xmlElementTree.SubElement(xmlCampaign, 'Notes').text = self.CampaignNotes
      
      xmlForOutput = xmlElementTree.ElementTree(xmlCampaign)
      self._indent(xmlForOutput.getroot())
      xmlForOutput.write(strFileName)
    except:
      pass

  def _load_xml(self, strFileName):
    """
      loads up an xml file of the appropriate format and populates the campaign attributes. 
    Arguments:
    Specifics:
    """
    try:
      objXMLTree = xmlElementTree.parse(strFileName)
      root = objXMLTree.getroot()
      self.Name = root.attrib['name']
      if root.attrib['active'] == 'True':
        self.ActiveCampaign = True
      else:
        self.ActiveCampaign = False
      self.Description = root[0].text
      self.Referee = root[1].text
      self.StartDate = root[2].text
      self.Setting = root[3].text
      self.CampaignNotes = root[6].text
      
      self.CampaignLog = [[xmlLogEntry.attrib['EntryDate'], xmlLogEntry.find('LogEntryPlayer').text, xmlLogEntry.find('LogEntryReferee').text] for xmlLogEntry in objXMLTree.iter('LogEntry')]
      
      self.AssetStore = [[xmlAsset.find('AssetName').text, xmlAsset.find('AssetDescription').text] for xmlAsset in objXMLTree.iter('Asset')]
    except:
      pass


# in-place prettyprint formatter

  def _indent(self, elem, level=0):
    #print('in _indent', elem.text, level)
    i = "\n" + level*"  "
    #print(elem.text, 'beg i', i, 'end i')
    #print('"', i, '"')
    if len(elem):
      #print('in if 1')
      if not elem.text or not elem.text.strip():
        #print('in if 1a')
        elem.text = i + "  "
      if not elem.tail or not elem.tail.strip():
        #print('in if 1b')
        elem.tail = i
      for elem in elem:
        #print('in for', level)
        self._indent(elem, level+1)
      if not elem.tail or not elem.tail.strip():
        #print('in if 1c')
        elem.tail = i
    else:
      #print('in else')
      if level and (not elem.tail or not elem.tail.strip()):
        #print('in else if')
        elem.tail = i
#//---------------------------------------------------------------------------------
#//-----------------------------Class Exception Definitions-------------------------
#//---------------------------------------------------------------------------------
