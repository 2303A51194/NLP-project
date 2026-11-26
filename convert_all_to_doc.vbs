Set fso = CreateObject("Scripting.FileSystemObject")
curDir = fso.GetAbsolutePathName(".")
desktopDir = "C:\Users\hp\OneDrive\Desktop"

docxThesis = curDir & "\Project_Documentation\Complete_Project_Documentation.docx"
docRootThesis = curDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal_Report.doc"
docRootAlt = curDir & "\Project_Report.doc"
docDesktopThesis = desktopDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal_Report.doc"
docDesktopAlt = desktopDir & "\Warangal_Hospital_Quality_NLP_Report.doc"

docFolder1 = desktopDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal\2_Project_Documentation\B.Tech_Project_Report_Final_Thesis.doc"
docFolder2 = desktopDir & "\Warangal_HealthRAG_Project_Documentation\B.Tech_Project_Report_Final_Thesis.doc"
docFolder3 = desktopDir & "\Warangal_HealthRAG_Project_Documentation\B.Tech_Project_Report_RAG_Warangal_Medical_System.doc"
docFolder4 = desktopDir & "\MediSense_NLP_Project\3_Project_Documentation\B.Tech_Project_Report_Final_Thesis.doc"

Set word = CreateObject("Word.Application")
word.Visible = False
word.DisplayAlerts = False

WScript.Echo "Opening Complete Project Thesis in MS Word..."
Set doc = word.Documents.Open(docxThesis)

WScript.Echo "Saving as Word 97-2003 Binary .doc format..."
doc.SaveAs docRootThesis, 0
doc.Close

WScript.Echo "Copying to all project locations..."
fso.CopyFile docRootThesis, docRootAlt, True
fso.CopyFile docRootThesis, docDesktopThesis, True
fso.CopyFile docRootThesis, docDesktopAlt, True

If fso.FolderExists(desktopDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal\2_Project_Documentation") Then
    fso.CopyFile docRootThesis, docFolder1, True
End If

If fso.FolderExists(desktopDir & "\Warangal_HealthRAG_Project_Documentation") Then
    fso.CopyFile docRootThesis, docFolder2, True
    fso.CopyFile docRootThesis, docFolder3, True
End If

If fso.FolderExists(desktopDir & "\MediSense_NLP_Project\3_Project_Documentation") Then
    fso.CopyFile docRootThesis, docFolder4, True
End If

' Copy IEEE Research Paper .doc
paperDoc = curDir & "\IEEE_Research_Paper.doc"
If fso.FileExists(paperDoc) Then
    fso.CopyFile paperDoc, desktopDir & "\IEEE_Research_Paper.doc", True
    If fso.FolderExists(desktopDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal\2_Project_Documentation") Then
        fso.CopyFile paperDoc, desktopDir & "\NLP_Based_Hospital_Service_Quality_Analysis_Warangal\2_Project_Documentation\IEEE_Research_Paper.doc", True
    End If
    If fso.FolderExists(desktopDir & "\Warangal_HealthRAG_Project_Documentation") Then
        fso.CopyFile paperDoc, desktopDir & "\Warangal_HealthRAG_Project_Documentation\IEEE_Research_Paper.doc", True
    End If
    If fso.FolderExists(desktopDir & "\MediSense_NLP_Project\3_Project_Documentation") Then
        fso.CopyFile paperDoc, desktopDir & "\MediSense_NLP_Project\3_Project_Documentation\IEEE_Research_Paper.doc", True
    End If
End If

word.Quit
WScript.Echo "ALL .DOC FILES CONVERTED AND DEPLOYED SUCCESSFULLY!"
