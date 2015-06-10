#// clsCharacter.py - The Character class is for containing basic data for PCs and NPCs
	
#//---------------------------------------------------------------------------------
#//-----------------------------Module Packages to be imported----------------------
#//---------------------------------------------------------------------------------
import ui, os
import console
import xml.etree.ElementTree as xmlElementTree

#//---------------------------------------------------------------------------------
#//-----------------------------Class Definitions-----------------------------------
#//---------------------------------------------------------------------------------
class clsCharacter:
  """ 
    Attributes:
    Methods:
    Exceptions:
  """ 

  def __init__(self, Name, Age, Race, HomeWorld, PlayerCharacter = True):
    """
      The class initialise function
      Arguments:
      Specifics:
    """

    try:
      #print('in init')
      self.character_name = Name
      self.character_age = Age
      self.character_race = Race
      self.character_home_world = HomeWorld
      self.character_player_character = PlayerCharacter

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Attribute Defintions--------------------------------
  def set_character_name(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_name = NewValue

    except:
      pass

  def get_character_name(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_name

    except:
      pass

  def set_character_age(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_age = NewValue

    except:
      pass

  def get_character_age(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_age

    except:
      pass

  def set_character_race(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_race = NewValue

    except:
      pass

  def get_character_race(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_race

    except:
      pass

  def set_character_home_world(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
      
    try:
      self.character_home_world = NewValue

    except:
      pass

  def get_character_home_world(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_home_world

    except:
      pass

  def set_character_player_character(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_player_character = NewValue

    except:
      pass

  def get_character_player_character(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_player_character

    except:
      pass

  def set_character_skills(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_skills = NewValue

    except:
      pass
    
  def get_character_skills(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_skills

    except:
      pass

  def set_character_weapons(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_weapons = NewValue

    except:
      pass

  def get_character_weapons(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_weapons

    except:
      pass

  def set_character_equipment(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_equipment = NewValue

    except:
      pass

  def get_character_equipment(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_equipment

    except:
      pass

  def set_character_strength(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_strength = NewValue

    except:
      pass
    
  def get_character_strength(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_strength

    except:
      pass

  def set_character_dexterity(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
      
    try:
      self.character_dexterity = NewValue

    except:
      pass

  def get_character_dexterity(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_dexterity

    except:
      pass

  def set_character_endurance(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_endurance = NewValue

    except:
      pass

  def get_character_endurance(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_endurance

    except:
      pass

  def set_character_intelligence(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_intelligence = NewValue

    except:
      pass
    
  def get_character_intelligence(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_intelligence
  	
    except:
      pass

  def set_character_education(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_education = NewValue

    except:
      pass

  def get_character_education(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_education

    except:
      pass

  def set_character_social(self, NewValue):
    """
      To set attribute ????????? value
      Arguments: 
      					NewValue: The new value which the attribute will be set to.
      Specifics:
    """
  
    try:
      self.character_social = NewValue

    except:
      pass

  def get_character_social(self):
    """
      To get attribute ????????? value
      Arguments: 
      Specifics:
    """
  
    try:
      return self.character_social

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Method Defintions-----------------------------------

  def save(self, SourceDest = 'xml', CampaignDataDirectory = '/Data/Characters/'):
    """
    Adds a fresh log entry at the end of the log list
    Arguments:
    Specifics:
    """
    try:
      print('in save', CampaignDataDirectory)
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
  def _save_xml(self, CharacterDataDirectory):
    """
      saves the campaign attributes into an xml file. 
    Arguments:
    Specifics:
    """
    try:
      print('in _save_xml', CharacterDataDirectory)
      strFileName = os.getcwdu() + CharacterDataDirectory + self.character_name +'.xml'
      print(strFileName)

      if self.character_player_character:
        xmlCharacter = xmlElementTree.Element('TravellerCharacter', name = self.character_name, age = self.character_age, race = self.character_race, homeworld = self.character_home_world, playercharacter = 'True')
      else:
        xmlCharacter = xmlElementTree.Element('TravellerCharacter', name = self.character_name, age = self.character_age, race = self.character_race, homeworld = self.character_home_world, playercharacter = 'False')


      #xmlDescription = xmlElementTree.SubElement(xmlCampaign, 'Description').text = self.Description
      #xmlReferee = xmlElementTree.SubElement(xmlCampaign, 'Referee').text = self.Referee
      #xmlStartDate = xmlElementTree.SubElement(xmlCampaign, 'StartDate').text = self.StartDate
      #xmlSetting = xmlElementTree.SubElement(xmlCampaign, 'Setting').text = self.Setting
      #xmlLog = xmlElementTree.SubElement(xmlCampaign, 'Log')
      #for Entry in self.CampaignLog:
      #  xmlLogEntry = xmlElementTree.SubElement(xmlLog, 'LogEntry', EntryDate = Entry[0])
      #  xmlElementTree.SubElement(xmlLogEntry, 'LogEntryPlayer').text = Entry[1]
      #  xmlElementTree.SubElement(xmlLogEntry, 'LogEntryReferee').text = Entry[2]
      
      #xmlAssets = xmlElementTree.SubElement(xmlCampaign, 'Assets')
      #for Asset in self.AssetStore:
      #  xmlAsset = xmlElementTree.SubElement(xmlAssets, 'Asset')
      #  xmlElementTree.SubElement(xmlAsset, 'AssetName').text = Asset[0]
      #  xmlElementTree.SubElement(xmlAsset, 'AssetDescription').text = Asset[1]
      
      #xmlNotes = xmlElementTree.SubElement(xmlCampaign, 'Notes').text = self.CampaignNotes
      
      xmlForOutput = xmlElementTree.ElementTree(xmlCharacter)
      #self._indent(xmlForOutput.getroot())
      xmlForOutput.write(strFileName)
    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Class Exception Definitions-------------------------
#//---------------------------------------------------------------------------------
	
