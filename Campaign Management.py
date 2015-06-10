"""
  Campaign Management.py - This provides the interface for the referee to manage various aspects of a campaign. this will include maintaining a campaign log, development of adventure ideas, managing campaign resources such as maps images, messages.
"""
#//--------------------------------------------------------------
#//--------------- Modules/Packages to be imported --------------
#//--------------------------------------------------------------
import ui, os
import console

#//--------------------------------------------------------------
#//--------------- Class Modules to be imported -----------------
#//--------------------------------------------------------------
import clsCampaign
import clsCampaignLogDataSource
import clsCampaignAssetsDataSource
reload(clsCampaign)
reload(clsCampaignLogDataSource)
reload(clsCampaignAssetsDataSource)

#//--------------------------------------------------------------
#//--------------- Class Definitions ----------------------------
#//--------------------------------------------------------------
class clsCampaignManagementView:
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
    CAMPAIGN_DATA_DIRECTORY = '/Data/Campaigns/'

    try:
      strCampaignManagementViewName = 'Campaign Management'
      self.vwInterface = ui.load_view(strCampaignManagementViewName)
      self.vwInterface.name = strCampaignManagementViewName
      self.objCampaignData = clsCampaign.clsCampaign()
      self._SelectedLogEntry = -1
      
      self._initialise_campaign_interface()
      self._initialise_control_handlers()
      
      self.vwInterface['tblCampaigns'].data_source.items = os.listdir(os.getcwdu() + CAMPAIGN_DATA_DIRECTORY)
      
      if Test:
        #self.objCampaignData = initialise_test_data()
        #self.objCampaignData.save('xml', CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)
        pass

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
    if tableview.name == 'tblCampaigns':
      #if not self.objCampaignData.get_name() == '':
      #  print('in select campaign data if')
      #  self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)
      self._load_data(tableview.data_source.items[row])
      self._load_interface_with_campaign_data()
    elif tableview.name == 'tblCampaignLog':
      pass

  def tableview_accessory_button_tapped(self, tableview, section, row):
    # Called when a row was selected.
    #print(tableview.name)
    if tableview.name == 'tblCampaigns':
      pass
    elif tableview.name == 'tblCampaignLog':
      self.vwInterface['vwRowEdit'].hidden = False
      self.vwInterface['vwRowEdit'].width = self.vwInterface['tblCampaignLog'].width
      self.vwInterface['vwRowEdit']['txtLogEntryDate'].hidden = True
      self.vwInterface['vwRowEdit']['lblLogEntryDate'].hidden = False
      self.vwInterface['vwRowEdit']['lblLogEntryDate'].text = self.objCampaignData.CampaignLog[row][0]
      self.vwInterface['vwRowEdit']['txtLogEntryPlayer'].text = self.objCampaignData.CampaignLog[row][1]
      self.vwInterface['vwRowEdit']['txtLogEntryReferee'].text = self.objCampaignData.CampaignLog[row][2]
      self._SelectedLogEntry = row
    
  def tableview_did_deselect(self, tableview, section, row):
    # Called when a row was de-selected (in multiple selection mode).
    pass

  def tableview_title_for_delete_button(self, tableview, section, row):
    # Return the title for the 'swipe-to-***' button.
    return 'Delete'

#// the textview delegate methods-----------------------------------------------

  def textview_should_begin_editing(self, textview):
    return True

  def textview_did_begin_editing(self, textview):
    pass

  def textview_did_end_editing(self, textview):
    pass

  def textview_should_change(self, textview, range, replacement):
    return True

  def textview_did_change(self, textview):
	  self.objCampaignData.set_campaign_notes(self.vwInterface['txtCampaignNotes'].text)
	  self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)

  def textview_did_change_selection(self, textview):
    pass

#//---------------------------------------------------------------------------------
#//-----------------------------Internal Method Defintions--------------------------

#// simple control handlers ----------------------------------------------

  def _btnAddLogEntry_handler(self, sender):
    """ 
	    	handles taps on the add log entry button. 
	    	Arguments: 
	    	Specifics:
	  """ 
    try:
	    #vwInterface = sender.superview
      if self._SelectedLogEntry == -1:
        self.vwInterface['vwRowEdit'].hidden = False
        self.vwInterface['vwRowEdit']['txtLogEntryDate'].hidden = False
        self.vwInterface['vwRowEdit']['lblLogEntryDate'].hidden = True
        self.vwInterface['vwRowEdit']['txtLogEntryPlayer'].text = ''
        self.vwInterface['vwRowEdit']['txtLogEntryReferee'].text = ''
        self.vwInterface['vwRowEdit'].width = self.vwInterface['tblCampaignLog'].width
        
    except:
	    pass

  def _btnCampaignStart_handler(self, sender):
    """ 
	    	handles taps on the button for date control to display date picker. 
	    	Arguments: 
	    	Specifics:
	  """ 
    try:
	    #vwInterface = sender.superview
	    if self.vwInterface['dteCampaignStart'].hidden:
	      self.vwInterface['dteCampaignStart'].hidden = False
	    else:
	      self.vwInterface['dteCampaignStart'].hidden = True
	      self.vwInterface['txtStartDate'].text = self.vwInterface['dteCampaignStart'].date.strftime('%d/%m/%Y')

    except:
	    pass

  def _btnCampaignLogEditCancel_handler(self, sender):
    """ 
	  	  handles taps on the button cancelling adding/making changes to a log entry
	  	  Arguments: 
	  	  Specifics:
	  """ 
    try:
	    vwLogEntryEdit = sender.superview
	    vwLogEntryEdit.hidden = True 
	    self._SelectedLogEntry = -1

    except:
	    pass

  def _btnCampaignLogEditSubmit_handler(self, sender):
    """ 
	  	  handles taps on the button for submitting adding/making changes to a log entry 
	  	  Arguments: 
	  	  Specifics:
	  """ 
    try:
      vwLogEntryEdit = sender.superview
      Row = self._SelectedLogEntry
      if Row == -1:
        strDate = vwLogEntryEdit['txtLogEntryDate'].text
        strPlayer = vwLogEntryEdit['txtLogEntryPlayer'].text
        strReferee = vwLogEntryEdit['txtLogEntryReferee'].text
        lstLogEntry = [strDate, strPlayer, strReferee]
        self.objCampaignData.CampaignLog.insert(0, lstLogEntry)
      else:
        self.objCampaignData.CampaignLog[Row][1] = vwLogEntryEdit['txtLogEntryPlayer'].text
        self.objCampaignData.CampaignLog[Row][2] = vwLogEntryEdit['txtLogEntryReferee'].text

      self.vwInterface['tblCampaignLog'].reload()
      self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)
      vwLogEntryEdit.hidden = True 
      self._SelectedLogEntry = -1

    except:
	    pass

  def _txtDescription_handler(self, sender):
    """ 
	  	handles changes to the campaign description. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    #print(self.objCampaignData.get_description())
	    self.objCampaignData.set_description(self.vwInterface['txtDescription'].text)
	    #print(self.objCampaignData.get_description())
	    self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)

    except:
	    pass

  def _txtSetting_handler(self, sender):
    """ 
	  	handles changes to the campaign setting. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    self.objCampaignData.set_setting(self.vwInterface['txtSetting'].text)
	    self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)

    except:
	    pass

  def _txtReferee_handler(self, sender):
    """ 
	  	handles changes to the campaign referee. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    self.objCampaignData.set_referee(self.vwInterface['txtReferee'].text)
	    self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)

    except:
	    pass

  def _txtCampaignNotes_handler(self, sender):
    """ 
	  	handles changes to the campaign referee. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    self.objCampaignData.set_campaign_notes(self.vwInterface['txtCampaignNotes'].text)
	    self.objCampaignData.save(CampaignDataDirectory = CAMPAIGN_DATA_DIRECTORY)

    except:
	    pass

  def _segCampaign_handler(self, sender):
    """ 
	  	handles taps on the segment control to display different views. 
	  	Arguments: 
	  	Specifics:
	  """ 
    try:
	    #vwInterface = sender.superview
	    tblCampaignLog = self.vwInterface['tblCampaignLog']
	    tblCampaignAssets = self.vwInterface['tblCampaignAssets']
	    txtCampaignNotes = self.vwInterface['txtCampaignNotes']
	    if sender.selected_index == 0:
	      txtCampaignNotes.hidden = True
	      tblCampaignLog.hidden = False
	      tblCampaignAssets.hidden = True
	    elif sender.selected_index == 1:
	      txtCampaignNotes.hidden = True
	      tblCampaignLog.hidden = True
	      tblCampaignAssets.hidden = False
	    elif sender.selected_index ==2:
	      tblCampaignLog.hidden = True
	      txtCampaignNotes.hidden = False
	      tblCampaignAssets.hidden = True
	    else:
	      pass

    except:
	    pass

  def _initialise_campaign_interface(self):
    """ 
	    	sets up the basics of the interface at launch.
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self.vwInterface['dteCampaignStart'].hidden = True
      self.vwInterface['vwRowEdit'].hidden = True
      btnAddCampaign = ui.ButtonItem('Add Campaign')
      self.vwInterface.left_button_items = (btnAddCampaign,)
      btnAddLogEntry = ui.ButtonItem('Add Log Entry', action = self._btnAddLogEntry_handler, enabled = False)
      btnAddAsset = ui.ButtonItem('Add Asset', enabled = False)
      self.vwInterface.right_button_items = (btnAddLogEntry,btnAddAsset)
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
      self.vwInterface['btnCampaignStart'].enabled = False
      self.vwInterface.right_button_items[0].enabled = False
      self.vwInterface.right_button_items[1].enabled = False
      self.vwInterface['txtDescription'].enabled = False
      self.vwInterface['txtReferee'].enabled = False
      self.vwInterface['txtStartDate'].enabled = False
      self.vwInterface['txtSetting'].enabled = False
      self.vwInterface['swActive'].enabled = False
      self.vwInterface['segCampaign'].enabled = False
      self.vwInterface['tblCampaignLog'].enabled = False
      self.vwInterface['tblCampaignAssets'].enabled = False
      self.vwInterface['txtCampaignNotes'].enabled = False

    except:
      pass

  def _enable_campaign_controls(self):
    """ 
	    	Enables the campaign content controls so they can be used
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self.vwInterface['btnCampaignStart'].enabled = True
      self.vwInterface.right_button_items[0].enabled = True
      self.vwInterface.right_button_items[1].enabled = True
      self.vwInterface['txtDescription'].enabled = True
      self.vwInterface['txtReferee'].enabled = True
      self.vwInterface['txtStartDate'].enabled = True
      self.vwInterface['txtSetting'].enabled = True
      self.vwInterface['swActive'].enabled = True
      self.vwInterface['segCampaign'].enabled = True
      self.vwInterface['tblCampaignLog'].enabled = True
      self.vwInterface['tblCampaignAssets'].enabled = True
      self.vwInterface['txtCampaignNotes'].enabled = True

    except:
      pass

  def _initialise_control_handlers(self):
    """ 
	    	sets up the methods to be used to handle interactions with the user interface. 
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      self.vwInterface['tblCampaigns'].delegate = self
      self.vwInterface['tblCampaignLog'].delegate = self
      self.vwInterface['txtCampaignNotes'].delegate = self
      self.vwInterface['segCampaign'].action = self._segCampaign_handler
      self.vwInterface['btnCampaignStart'].action = self._btnCampaignStart_handler
      self.vwInterface['vwRowEdit']['btnCancel'].action = self._btnCampaignLogEditCancel_handler
      self.vwInterface['vwRowEdit']['btnSubmit'].action = self._btnCampaignLogEditSubmit_handler
      self.vwInterface['txtDescription'].action = self._txtDescription_handler
      self.vwInterface['txtSetting'].action = self._txtSetting_handler
      self.vwInterface['txtReferee'].action = self._txtReferee_handler
    except:
      pass

  def _load_data(self, strCampaignName):
    """ 
	    	Loads campaign data from file.
	    	Arguments: 
	  	Specifics:
	  """ 
	  
    try:
      strFileName = os.getcwdu() + CAMPAIGN_DATA_DIRECTORY + strCampaignName
      self.objCampaignData.load(strFileName, 'xml')

    except:
      pass

  def _load_interface_with_campaign_data(self):
    """ 
	    	Sets the basic data (description, referee, etc.) in the interface. 
	    	Arguments: 
	    	Specifics:
	  """ 
	  
    try:
      self._enable_campaign_controls()
      self.vwInterface['txtDescription'].text = self.objCampaignData.get_description()
      self.vwInterface['txtReferee'].text = self.objCampaignData.get_referee()
      self.vwInterface['txtStartDate'].text = self.objCampaignData.get_start_date()
      self.vwInterface['txtSetting'].text = self.objCampaignData.get_setting()
      self.vwInterface['swActive'].value = self.objCampaignData.get_active_campaign()
      
      # These data sources will need to be actually linked to the campaign data for deletion purposes
      lstLogSectionText = ['date | player Info | referee Info']
      self.vwInterface['tblCampaignLog'].data_source = clsCampaignLogDataSource.clsCampaignLogDataSource(self.objCampaignData.CampaignLog, lstLogSectionText) #get_campaign_log()
      self.vwInterface['tblCampaignLog'].reload()
      
      lstAssetSectionText = ['Asset | Description']
      self.vwInterface['tblCampaignAssets'].data_source = clsCampaignAssetsDataSource.clsCampaignAssetsDataSource(self.objCampaignData.get_asset_store(), lstAssetSectionText)
      self.vwInterface['tblCampaignAssets'].reload()
      
      self.vwInterface['txtCampaignNotes'].text = self.objCampaignData.get_campaign_notes()
      
      if self.vwInterface['segCampaign'].selected_index == 0:
        self.vwInterface['txtCampaignNotes'].hidden = True
        self.vwInterface['tblCampaignLog'].hidden = False
        self.vwInterface['tblCampaignAssets'].hidden = True
      elif vwInterface['segCampaign'].selected_index == 1:
        self.vwInterface['txtCampaignNotes'].hidden = True
        self.vwInterface['tblCampaignLog'].hidden = True
        self.vwInterface['tblCampaignAssets'].hidden = False      
      elif vwInterface['segCampaign'].selected_index ==2:
        self.vwInterface['txtCampaignNotes'].hidden = False
        self.vwInterface['tblCampaignLog'].hidden = True
        self.vwInterface['tblCampaignAssets'].hidden = True
      else:
	      pass
	    
      #print(dir(self.objCampaignData))
      
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
#//--------------- Function Definitions -------------------------
#//--------------------------------------------------------------
def initialise_test_data():
  """ 
	  	Creates some basic campaign data for test purposes.
	  	Arguments: 
	  	Specifics:
	""" 
	  
  try:
    # create data for the log, this will have date, player's info, referee's info, possibly
    # then character log data, but stick to the first 3 for now.
    lstTestLog = []
    lstAssetStore = []
    for cntLoop in range(1, 5):
      strDate = '10' + str(cntLoop) + '/1105'
      strPlayer = 'Player' + str(cntLoop)
      strReferee = 'Referee' + str(cntLoop)
      lstLogEntry = [strDate, strPlayer, strReferee]
      lstTestLog.append(lstLogEntry)
      
      strAssetName = 'Asset' + str(cntLoop)
      strAssetDescription = 'The number ' + str(cntLoop) + ' asset'
      lstAsset = [strAssetName, strAssetDescription]
      lstAssetStore.append(lstAsset)

    strCampaignNotes = '''these would be notes for developing the campaign
    
    they would have all of the ideas for coming adventures
    
    character ideas
    
    installations,
    
    and even possible new toys for the player characters. '''
    
    objTestCampaign = clsCampaign.clsCampaign('The Online Campaign', 'some more Test Campaign Data', 'Simon Snowden', '13/05/2015', 'The Third Imperium after the 5th Frontier War', lstTestLog, lstAssetStore, strCampaignNotes, True)
    objTestCampaign.append_campaign_log_entry('123/1105', 'the stuff players know', 'the stuff the referee knows and needs to keep track of')

    return objTestCampaign
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
    objCampaignManagementView = clsCampaignManagementView()
    objCampaignManagementView.present_view()
    #print(dir(clsCampaignManagementView))
  except:
	  pass

if __name__ == '__main__':
	main()

