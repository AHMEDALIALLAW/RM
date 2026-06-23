import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
        
        tree = ET.fromstring(xml_content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = tree.findall('.//w:p', ns)
        text = []
        for p in paragraphs:
            texts = p.findall('.//w:t', ns)
            if texts:
                text.append(''.join(t.text for t in texts))
            else:
                text.append('')
                
        return '\n'.join(text)
    except Exception as e:
        return str(e)

print(extract_text_from_docx(r"C:\Users\THINKPAD\Desktop\ResearchShalaiby\PROJECTRM\CH1-3.docx"))
