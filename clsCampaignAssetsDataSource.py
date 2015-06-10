#// clsCampaignDataSource.py - The clsCampaignDataSource class is the data source implementation for the Campaign Management View table view.
import ui

class clsCampaignAssetsDataSource:
  """
      Attributes:
      Methods:
      Exceptions:
  """

  def __init__(self, lstCampaignTableViewData, HeaderTitle):
    """
      The class initialise function
      Arguments:
      Specifics:
    """
    try:
      #print('In data source init')
      self.NumSections = len(HeaderTitle)
      self.HeaderTitle = HeaderTitle
      self.NumRows = len(lstCampaignTableViewData)
      self.RowText = lstCampaignTableViewData
    except:
      pass

#//---------------------------------------------------------------------------------
#//-----------------------------Attribute Defintions--------------------------------
  def tableview_number_of_sections(self, tableview):
    # Return the number of sections (defaults to 1)
    return self.NumSections

  def tableview_number_of_rows(self, tableview, section):
    # Return the number of rows in the section
    return self.NumRows

  def tableview_cell_for_row(self, tableview, section, row):
    # Create and return a cell for the given section/row
    cell = ui.TableViewCell()
    WhichElement = 1
    
    for Element in self.RowText[row]:
      lblLog = ui.Label()
      lblLog.border_width = 1
      lblLog.height = cell.height
      if WhichElement == 1:
        lblLog.x = 0
        lblLog.width = 200
      elif WhichElement == 2:
        lblLog.x = 204
        lblLog.width = 500
        
      lblLog.text = ' ' + Element
      cell.content_view.add_subview(lblLog)
      WhichElement += 1

    cell.accessory_type = 'detail_button'
    return cell

  def tableview_title_for_header(self, tableview, section):
    # Return a title for the given section.
    # If this is not implemented, no section headers will be shown.
    strHeaderTitle = self.HeaderTitle[section]
    return strHeaderTitle

  def tableview_can_delete(self, tableview, section, row):
    # Return True if the user should be able to delete the given row.
    return True

  def tableview_can_move(self, tableview, section, row):
    # Return True if a reordering control should be shown for the given row (in editing mode).
    return False

  def tableview_delete(self, tableview, section, row):
    # Called when the user confirms deletion of the given row.
    pass

  def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
    # Called when the user moves a row with the reordering control (in editing mode).
    pass

#//---------------------------------------------------------------------------------
#//-----------------------------Method Defintions-----------------------------------


#//---------------------------------------------------------------------------------
#//-----------------------------Internal Method Defintions--------------------------
