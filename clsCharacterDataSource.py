#// clsCharacterDataSource.py - The clsCharacterDataSource class is the data source implementation for the Character Management View table view.
import ui
import console

class clsCharacterDataSource:
  """
      Attributes:
      Methods:
      Exceptions:
  """

  def __init__(self, lstCharacterTableViewData, HeaderTitle):
    """
      The class initialise function
      Arguments:
      Specifics:
    """
    try:
      self.NumSections = len(HeaderTitle)
      self.HeaderTitle = HeaderTitle
      self.NumRows = len(lstCharacterTableViewData)
      self.RowText = lstCharacterTableViewData
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
    #txtDate = ui.TextField()
    #txtDate.height = cell.height
    #txtDate.width = cell.width
    #txtDate.text = self.RowText[row][0]
    #cell.add_subview(txtDate)
    #txtLog = ui.TextField()
    #txtLog.height = cell.height
    #txtLog.width = cell.width
    #txtLog.text = self.RowText[row][1] + ' ' + self.RowText[row][2]
    #cell.content_view.add_subview(txtLog)
    strRowText = ''
    cell = ui.TableViewCell()
    for Element in self.RowText[row]:
      strRowText += Element + ' '
    
    cell.text_label.text = strRowText
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
