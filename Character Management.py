"""
  Character Management.py - this allows the user to manage all aspects of character information.
"""
#//--------------------------------------------------------------
#//--------------- Modules/Packages to be imported --------------
#//--------------------------------------------------------------
import ui, os
import console

#//--------------------------------------------------------------
#//--------------- Class Modules to be imported -----------------
#//--------------------------------------------------------------
import clsCharacter
import clsCharacterDataSource
reload(clsCharacter)
reload(clsCharacterDataSource)
#import clsCharacterListDelegate


#//---------------------------------------------------------------------------------
#//-----------------------------Class Definitions-----------------------------------
#//---------------------------------------------------------------------------------
"""
  This provides the interface for the character mangagement aspects of the app.
"""
class clsCharacterManagement:
  """
  Attributes:
  Methods:
  Exceptions:
  """

  def __init__(self, Test = False):
    """
    The class initialise function that sets up the view and handles test conditions if requested
    Arguments:
    Specifics:
    """
    global CAMPAIGN_DATA_DIRECTORY
    global SKILLS_SELECTED, WEAPONS_SELECTED, EQUIPMENT_SELECTED
    global CHARACTERISTICS_SELECTED, ARMOUR_SELECTED, NOTES_SELECTED
    global CHARACTERISTIC_ORIGINAL, CHARACTERISTIC_MAX, CHARACTERISTIC_CURRENT, SLIDER_INCREMENT
    CHARACTER_DATA_DIRECTORY = '/Data/Character/'
    SKILLS_SELECTED = 0
    WEAPONS_SELECTED = 1
    EQUIPMENT_SELECTED = 2
    CHARACTERISTICS_SELECTED = 0
    ARMOUR_SELECTED = 1
    NOTES_SELECTED = 2
    CHARACTERISTIC_ORIGINAL = 0
    CHARACTERISTIC_MAX = 1
    CHARACTERISTIC_CURRENT = 2
    SLIDER_INCREMENT = 20

    try:
      strViewName = 'Character Management'    
      self.vwInterface = ui.load_view(strViewName)
      self.vwInterface.name = strViewName
      self._initialise_control_handlers()

      if Test:
        self.objCharacter = self._intialising_character_test_data()
        self._load_interface_with_character_data()
        self._load_interface_with_characteristics()
        self.vwInterface['tblSkills'].data_source = self._initialise_character_skills_data_source(self.objCharacter.get_character_skills())
        self.objCharacter.save()

    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Attribute Defintions--------------------------------

#//---------------------------------------------------------------------------------
#//-----------------------------Method Defintions-----------------------------------

  def present_view(self):
    """ 
	    Puts the campaign management view on screen. 
	    Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      if ui.get_screen_size()[1] >= 768:
        self.vwInterface.present('fullscreen')
      else:                                                 # iPhone 
	      self.vwInterface.present(orientations=['portrait'])

    except:
      pass

#// control handler methods------------------------------------------------------
#// -----------------------------------------------------------------------------

#// the tablewiew delegate methods-----------------------------------------------

  def tableview_did_select(self, tableview, section, row):
    # Called when a row was selected in a tableview.
    #print(tableview.name)
    if tableview.name == 'tblName1':
      pass
    elif tableview.name == 'tblName2':
      pass

  def tableview_accessory_button_tapped(self, tableview, section, row):
    # Called when a row was selected.
    #print(tableview.name)
    if tableview.name == 'tblName1':
      pass
    elif tableview.name == 'tblName2':
      pass
    
  def tableview_did_deselect(self, tableview, section, row):
    # Called when a row was de-selected (in multiple selection mode).
    pass

  def tableview_title_for_delete_button(self, tableview, section, row):
    # Return the title for the 'swipe-to-***' button.
    return 'Delete'

#//---------------------------------------------------------------------------------
#//-----------------------------Internal Method Defintions--------------------------

#// simple control handlers ----------------------------------------------

  def _typeControlName_handler(self, sender):
    """ 
	    	handles taps on the button for date control to display date picker. 
	    	Arguments: 
	    	Specifics:
	  """ 
    try:
      pass

    except:
	    pass

  def segCharacter2_handler(self, sender):
    """ 
	  	handles taps on the segment control to display different views. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    tblSkills = self.vwInterface['tblSkills']
	    if sender.selected_index == SKILLS_SELECTED:
	      tblSkills.hidden = False
	      tblSkills.data_source = self._initialise_character_skills_data_source(self.objCharacter.get_character_skills())
	      tblSkills.reload()
	    elif sender.selected_index == WEAPONS_SELECTED:
	      tblSkills.hidden = False
	      tblSkills.data_source = self._initialise_character_weapons_data_source(self.objCharacter.get_character_weapons())
	      tblSkills.reload()
	    elif sender.selected_index == EQUIPMENT_SELECTED:
	      tblSkills.hidden = False
	      tblSkills.data_source = self._initialise_character_equipment_data_source(self.objCharacter.get_character_equipment())
	      tblSkills.reload()
	    else:
	      pass
	  	
    except:
	    pass

  def segCharacter1_handler(self, sender):
    """ 
	  	handles taps on the segment control to display different views. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    vwInterface = sender.superview
	    scrCharacteristics = vwInterface['scrCharacteristics']
	    txtCharacter = vwInterface['txtCharacterNotes']
	    if sender.selected_index == CHARACTERISTICS_SELECTED:
	      scrCharacteristics.hidden = False
	      txtCharacter.hidden = True
	    elif sender.selected_index == ARMOUR_SELECTED:
	      scrCharacteristics.hidden = True
	      txtCharacter.hidden = True
	    elif sender.selected_index == NOTES_SELECTED:
	      scrCharacteristics.hidden = True
	      txtCharacter.hidden = False
	    else:
	      pass
	  	
    except:
	    pass

  def _initialise_name_interface(self):
    """ 
	    	sets up the basics of the interface at launch.
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self._disable_campaign_controls()

    except:
      pass

  def _disable_campaign_controls(self):
    """ 
	    	Disables the campaign content controls so they cannot be used. 
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      pass

    except:
      pass

  def _enable_campaign_controls(self):
    """ 
	    	Enables the campaign content controls so they can be used
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      pass

    except:
      pass

  def _initialise_control_handlers(self):
    """ 
	    	Loads campaign data from file.
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self.vwInterface['segCharacter1'].action = self.segCharacter1_handler
      self.vwInterface['segCharacter2'].action = self.segCharacter2_handler
      #self.vwInterface['tblCampaigns'].delegate = self
      #self.vwInterface['btnCampaignStart'].action = self._typeControlName_handler
      pass

    except:
      pass

  def _intialising_character_test_data(self):
    """ 
	   	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      objAndrewFletcher = clsCharacter.clsCharacter('Andrew Fletcher', '38', 'Human', 'Rhylanor/Rhylanor')
      CharacterSkills = [['Slug Rifle', '4']]
      CharacterSkills.append(['Streetwise', '2'])
      CharacterSkills.append(['Jack of All Trades', '1'])
      objAndrewFletcher.set_character_skills(CharacterSkills)

      CharacterWeapons = [['Blade', '4']]
      CharacterWeapons.append(['Gauss Pistol', '2'])
      CharacterWeapons.append(['Body Pistol', '1'])
      objAndrewFletcher.set_character_weapons(CharacterWeapons)
    
      CharacterEquipment = [['Comm', '4']]
      CharacterEquipment.append(['Smart Rope', '2'])
      CharacterEquipment.append(['Watch', '1'])
      objAndrewFletcher.set_character_equipment(CharacterEquipment)
      
      CharacterStrength = [7, 7, 1]
      objAndrewFletcher.set_character_strength(CharacterStrength)
      CharacterDexterity = [14, 14, 14]
      objAndrewFletcher.set_character_dexterity(CharacterDexterity)
      CharacterEndurance = [11, 11, 6]
      objAndrewFletcher.set_character_endurance(CharacterEndurance)
      CharacterIntelligence = [9, 9, 9]
      objAndrewFletcher.set_character_intelligence(CharacterIntelligence)
      CharacterEducation = [8, 8, 8]
      objAndrewFletcher.set_character_education(CharacterEducation)
      CharacterSocial = [5, 5, 5]
      objAndrewFletcher.set_character_social(CharacterSocial)
    
      return objAndrewFletcher
	  	
    except:
	    pass

  def _load_data(self, strCampaignName):
    """ 
	    	Loads campaign data from file.
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      pass

    except:
      pass

  def _load_interface_with_character_data(self):
    """ 
	  	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self.vwInterface['txtAge'].text = self.objCharacter.get_character_age()
      self.vwInterface['txtRace'].text = self.objCharacter.get_character_race()
      self.vwInterface['txtHomeWorld'].text = self.objCharacter.get_character_home_world()
    
    except:
	    pass

  def _load_interface_with_characteristics(self):
    """ 
	  	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      lstStrength = self.objCharacter.get_character_strength()
      self.vwInterface['scrCharacteristics']['btnStrengthOriginal'].title = str(lstStrength[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnStrengthMax'].title = str(lstStrength[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnStrengthCurrent'].title = str(lstStrength[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldStrength'].value = (float(lstStrength[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)
    
      lstDexterity = self.objCharacter.get_character_dexterity()
      self.vwInterface['scrCharacteristics']['btnDexterityOriginal'].title = str(lstDexterity[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnDexterityMax'].title = str(lstDexterity[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnDexterityCurrent'].title = str(lstDexterity[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldDexterity'].value = (float(lstDexterity[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)

      lstEndurance = self.objCharacter.get_character_endurance()
      self.vwInterface['scrCharacteristics']['btnEnduranceOriginal'].title = str(lstEndurance[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnEnduranceMax'].title = str(lstEndurance[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnEnduranceCurrent'].title = str(lstEndurance[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldEndurance'].value = (float(lstEndurance[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)

      lstIntelligence = self.objCharacter.get_character_intelligence()
      self.vwInterface['scrCharacteristics']['btnIntelligenceOriginal'].title = str(lstIntelligence[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnIntelligenceMax'].title = str(lstIntelligence[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnIntelligenceCurrent'].title = str(lstIntelligence[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldIntelligence'].value = (float(lstIntelligence[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)
    
      lstEducation = self.objCharacter.get_character_education()
      self.vwInterface['scrCharacteristics']['btnEducationOriginal'].title = str(lstEducation[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnEducationMax'].title = str(lstEducation[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnEducationCurrent'].title = str(lstEducation[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldEducation'].value = (float(lstEducation[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)

      lstSocial = self.objCharacter.get_character_social()
      self.vwInterface['scrCharacteristics']['btnSocialOriginal'].title = str(lstSocial[CHARACTERISTIC_ORIGINAL])
      self.vwInterface['scrCharacteristics']['btnSocialMax'].title = str(lstSocial[CHARACTERISTIC_MAX])
      self.vwInterface['scrCharacteristics']['btnSocialCurrent'].title = str(lstSocial[CHARACTERISTIC_CURRENT])
      self.vwInterface['scrCharacteristics']['sldSocial'].value = (float(lstSocial[CHARACTERISTIC_CURRENT]) / SLIDER_INCREMENT)
    except:
	    pass

  def _initialise_character_skills_data_source(self, lstCharacterSkills):
    """ 
	  	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
      strHeader = ['Skill | Level']
      return clsCharacterDataSource.clsCharacterDataSource(lstCharacterSkills, strHeader)
    except:
	    pass

  def _initialise_character_weapons_data_source(self, lstCharacterWeapons):
    """ 
	  	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
      strHeader = ['Weapon | Level']
      return clsCharacterDataSource.clsCharacterDataSource(lstCharacterWeapons, strHeader)
    except:
	    pass

  def _initialise_character_equipment_data_source(self, lstCharacterEquipment):
    """ 
	  	To do whatever the method does.
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
      strHeader = ['Equipment | Level']
      return clsCharacterDataSource.clsCharacterDataSource(lstCharacterEquipment, strHeader)
    except:
	    pass

  def _iphone_interface_layout(self):
    """ 
	    	Alters the layout to suit an iPhone. 
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      # first cal calculate proportions based on the golden ratio
      Proportion = 5
      BufferBetweenCampaignListAndContent = 30
      
      Width = ui.get_screen_size()[1]
      print(Width)
      ContentWidth = (Width / Proportion) * 4
      print(ContentWidth)
      CampaignListWidth = Width - ContentWidth
      print(CampaignListWidth)
      print(Width, ContentWidth, CampaignListWidth)
      ContentLeft = CampaignListWidth + BufferBetweenCampaignListAndContent
      
      self.vwInterface['tblCampaigns'].x = 0
      self.vwInterface['tblCampaigns'].width = CampaignListWidth
      self.vwInterface['segCampaign'].x = ContentLeft
      self.vwInterface['lblDescription'].x = ContentLeft

    except:
      pass

#//--------------------------------------------------------------
#//--------------- Main Body ------------------------------------
#//--------------------------------------------------------------

def main():
  """ 
	  	This starts the application.
	  	Arguments: 
	  	Specifics:
	""" 
  console.clear()
#//--------------------------------------------------------------
#//--------------- Global Variables -----------------------------
  #global 
  try:
    objCharacterManagement = clsCharacterManagement(True)
    objCharacterManagement.present_view()
  except:
	  pass

if __name__ == '__main__':
	main()

