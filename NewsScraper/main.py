from menubox import MyGUI

#Change  "Mozilla/5.0" to your broswer {Mozzilla/5.0}
MyGUI.headers = {'User-agent': 'Mozilla/5.0'}

#change what name of files u want
MyGUI.excel_save_data = "NewsData.xlsx"
MyGUI.txt_save_data = "NewsData.txt"

MyGUI()

