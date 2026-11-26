#!/usr/bin/env python3
"""
Builds SarkariPedia_Mini_Project_Report.docx matching the exact academic 33-page
structure of SarkariPedia_Mini_Project_Report.pdf (and the reference Timetable Report).

Leaves Student Name, Roll Number, and Supervisor Name as blank lines (anonymized).
Embeds all 14 high-resolution figures from docs/diagrams/ (including Fig. 5.5.1 and 5.6.1).
Formats tables, code blocks, callouts, running headers, and footers with page numbers.
"""

import os
import re
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DOCX = os.path.join(BASE_DIR, "SarkariPedia_Mini_Project_Report.docx")
DIAG_DIR = os.path.join(BASE_DIR, "diagrams")
MD_FILE = os.path.join(BASE_DIR, "SarkariPedia_Mini_Project_Report.md")

def xml_esc(s):
    if s is None:
        return ""
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))

class DocxBuilder:
    def __init__(self):
        self.body_xml = []
        self.images = []  # list of (rId, filename, filepath, cx, cy)
        self.img_counter = 0

    def add_p(self, text, align="both", bold=False, italic=False, size=22, 
              color="000000", font="Times New Roman", space_before=0, space_after=140, line=276):
        t = xml_esc(text)
        rpr = f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}"/>'
        if bold:
            rpr += '<w:b/>'
        if italic:
            rpr += '<w:i/>'
        if size:
            rpr += f'<w:sz w:val="{size}"/>'
        if color:
            rpr += f'<w:color w:val="{color}"/>'

        ppr = f'<w:spacing w:before="{space_before}" w:after="{space_after}" w:line="{line}" w:lineRule="auto"/>'
        if align:
            ppr += f'<w:jc w:val="{align}"/>'

        xml = f'<w:p><w:pPr>{ppr}</w:pPr><w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{t}</w:t></w:r></w:p>'
        self.body_xml.append(xml)

    def add_h1(self, text, space_before=360, space_after=180):
        t = xml_esc(text)
        xml = (f'<w:p><w:pPr><w:spacing w:before="{space_before}" w:after="{space_after}"/><w:jc w:val="center"/></w:pPr>'
               f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="28"/><w:color w:val="0D1B2A"/></w:rPr>'
               f'<w:t>{t}</w:t></w:r></w:p>')
        self.body_xml.append(xml)

    def add_h2(self, text, space_before=240, space_after=120):
        t = xml_esc(text)
        xml = (f'<w:p><w:pPr><w:spacing w:before="{space_before}" w:after="{space_after}"/><w:jc w:val="left"/></w:pPr>'
               f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="24"/><w:color w:val="1B263B"/></w:rPr>'
               f'<w:t>{t}</w:t></w:r></w:p>')
        self.body_xml.append(xml)

    def add_h3(self, text, space_before=180, space_after=80):
        t = xml_esc(text)
        xml = (f'<w:p><w:pPr><w:spacing w:before="{space_before}" w:after="{space_after}"/><w:jc w:val="left"/></w:pPr>'
               f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="22"/><w:color w:val="2C3E50"/></w:rPr>'
               f'<w:t>{t}</w:t></w:r></w:p>')
        self.body_xml.append(xml)

    def add_bullet(self, text, bold_prefix=None):
        ppr = '<w:pPr><w:ind w:left="720" w:hanging="360"/><w:spacing w:after="90"/><w:jc w:val="both"/></w:pPr>'
        bullet_run = '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="22"/></w:rPr><w:t xml:space="preserve">&#8226;   </w:t></w:r>'
        runs = [bullet_run]
        if bold_prefix:
            runs.append(f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="22"/></w:rPr><w:t xml:space="preserve">{xml_esc(bold_prefix)} </w:t></w:r>')
        runs.append(f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="22"/></w:rPr><w:t>{xml_esc(text)}</w:t></w:r>')
        xml = f'<w:p>{ppr}{"".join(runs)}</w:p>'
        self.body_xml.append(xml)

    def add_page_break(self):
        self.body_xml.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def add_callout(self, text):
        t = xml_esc(text)
        xml = (f'<w:p><w:pPr>'
               f'<w:pBdr>'
               f'<w:top w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/>'
               f'<w:left w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/>'
               f'<w:bottom w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/>'
               f'<w:right w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/>'
               f'</w:pBdr>'
               f'<w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>'
               f'<w:spacing w:before="120" w:after="120"/>'
               f'<w:jc w:val="center"/>'
               f'<w:ind w:left="240" w:right="240"/>'
               f'</w:pPr>'
               f'<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:b/><w:sz w:val="17"/><w:color w:val="0F172A"/></w:rPr>'
               f'<w:t xml:space="preserve">{t}</w:t></w:r></w:p>')
        self.body_xml.append(xml)

    def add_code_block(self, lines):
        for line in lines:
            t = xml_esc(line)
            xml = (f'<w:p><w:pPr>'
                   f'<w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="3B82F6"/></w:pBdr>'
                   f'<w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/>'
                   f'<w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/>'
                   f'<w:ind w:left="360" w:right="360"/>'
                   f'</w:pPr>'
                   f'<w:r><w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="17"/><w:color w:val="1E293B"/></w:rPr>'
                   f'<w:t xml:space="preserve">{t}</w:t></w:r></w:p>')
            self.body_xml.append(xml)

    def add_table(self, headers, rows, col_widths=None):
        total_w = 9746
        if not col_widths:
            w_per_col = total_w // len(headers)
            col_widths = [w_per_col] * len(headers)

        tbl_xml = ['<w:tbl>',
                   f'<w:tblPr><w:tblW w:w="{total_w}" w:type="dxa"/><w:jc w:val="center"/>',
                   '<w:tblBorders>',
                   '<w:top w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>',
                   '<w:left w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>',
                   '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>',
                   '<w:right w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>',
                   '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E5E5E5"/>',
                   '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="E5E5E5"/>',
                   '</w:tblBorders></w:tblPr>']

        tbl_xml.append('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>')
        for h, w in zip(headers, col_widths):
            tbl_xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="EBF0F7"/></w:tcPr>'
                           f'<w:p><w:pPr><w:jc w:val="left"/><w:spacing w:before="60" w:after="60"/></w:pPr>'
                           f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="19"/><w:color w:val="0D1B2A"/></w:rPr>'
                           f'<w:t>{xml_esc(h)}</w:t></w:r></w:p></w:tc>')
        tbl_xml.append('</w:tr>')

        for row in rows:
            tbl_xml.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>')
            for cell, w in zip(row, col_widths):
                tbl_xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/></w:tcPr>'
                               f'<w:p><w:pPr><w:jc w:val="left"/><w:spacing w:before="40" w:after="40"/></w:pPr>'
                               f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="18"/></w:rPr>'
                               f'<w:t>{xml_esc(cell)}</w:t></w:r></w:p></w:tc>')
            tbl_xml.append('</w:tr>')

        tbl_xml.append('</w:tbl>')
        tbl_xml.append('<w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>')
        self.body_xml.append("".join(tbl_xml))

    def add_image(self, filename, caption, max_width_in=6.4):
        filepath = os.path.join(DIAG_DIR, filename)
        if not os.path.exists(filepath):
            return

        im = Image.open(filepath)
        orig_w, orig_h = im.size

        cx = int(max_width_in * 914400)
        cy = int(cx * (orig_h / orig_w))

        max_cy = int(4.5 * 914400)
        if cy > max_cy:
            cy = max_cy
            cx = int(cy * (orig_w / orig_h))

        self.img_counter += 1
        rId = f"rIdImg{self.img_counter}"
        self.images.append((rId, filename, filepath, cx, cy))

        img_xml = (f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="140" w:after="60"/></w:pPr>'
                   f'<w:r><w:drawing>'
                   f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
                   f'<wp:extent cx="{cx}" cy="{cy}"/>'
                   f'<wp:effectExtent l="0" t="0" r="0" b="0"/>'
                   f'<wp:docPr id="{self.img_counter}" name="Figure {self.img_counter}"/>'
                   f'<wp:cNvGraphicFramePr>'
                   f'<a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>'
                   f'</wp:cNvGraphicFramePr>'
                   f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                   f'<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                   f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                   f'<pic:nvPicPr>'
                   f'<pic:cNvPr id="{self.img_counter}" name="Picture {self.img_counter}"/>'
                   f'<pic:cNvPicPr/>'
                   f'</pic:nvPicPr>'
                   f'<pic:blipFill>'
                   f'<a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rId}"/>'
                   f'<a:stretch><a:fillRect/></a:stretch>'
                   f'</pic:blipFill>'
                   f'<pic:spPr>'
                   f'<a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
                   f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
                   f'</pic:spPr>'
                   f'</pic:pic>'
                   f'</a:graphicData>'
                   f'</a:graphic>'
                   f'</wp:inline>'
                   f'</w:drawing></w:r></w:p>')
        self.body_xml.append(img_xml)

        cap_t = xml_esc(caption)
        cap_xml = (f'<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="40" w:after="160"/></w:pPr>'
                   f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="19"/><w:color w:val="1F2937"/></w:rPr>'
                   f'<w:t>{cap_t}</w:t></w:r></w:p>')
        self.body_xml.append(cap_xml)

    def build_docx(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
            ct_lines = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
                '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
                '  <Default Extension="xml" ContentType="application/xml"/>',
                '  <Default Extension="png" ContentType="image/png"/>',
                '  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
                '  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>',
                '  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>',
                '  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>',
                '  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
                '  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
                '</Types>'
            ]
            z.writestr('[Content_Types].xml', "\n".join(ct_lines))

            rels_lines = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
                '  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>',
                '  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>',
                '  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>',
                '</Relationships>'
            ]
            z.writestr('_rels/.rels', "\n".join(rels_lines))

            core_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',
                '  <dc:title>SarkariPedia Mini Project Report</dc:title>',
                '  <dc:subject>B.Tech CSE Mini Project Report - AKTU</dc:subject>',
                '  <dc:creator>Department of Computer Science &amp; Engineering, KIT Kanpur</dc:creator>',
                '  <cp:lastModifiedBy>SarkariPedia Word Generator</cp:lastModifiedBy>',
                '</cp:coreProperties>'
            ]
            z.writestr('docProps/core.xml', "\n".join(core_xml))

            app_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">',
                '  <Application>Microsoft Word</Application>',
                '  <Pages>33</Pages>',
                '</Properties>'
            ]
            z.writestr('docProps/app.xml', "\n".join(app_xml))

            doc_rels = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
                '  <Relationship Id="rIdHeader1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>',
                '  <Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>',
                '  <Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            ]
            for rId, filename, filepath, cx, cy in self.images:
                doc_rels.append(f'  <Relationship Id="{rId}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{filename}"/>')
            doc_rels.append('</Relationships>')
            z.writestr('word/_rels/document.xml.rels', "\n".join(doc_rels))

            for rId, filename, filepath, cx, cy in self.images:
                with open(filepath, "rb") as im_f:
                    z.writestr(f"word/media/{filename}", im_f.read())

            hdr_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">',
                '  <w:p>',
                '    <w:pPr>',
                '      <w:pBdr>',
                '        <w:bottom w:val="single" w:sz="4" w:space="4" w:color="CCCCCC"/>',
                '      </w:pBdr>',
                '    </w:pPr>',
                '    <w:r>',
                '      <w:rPr>',
                '        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>',
                '        <w:i/>',
                '        <w:sz w:val="18"/>',
                '        <w:color w:val="444444"/>',
                '      </w:rPr>',
                '      <w:t>SarkariPedia: Automated Indian Government Portals Directory &amp; Crawler</w:t>',
                '    </w:r>',
                '  </w:p>',
                '</w:hdr>'
            ]
            z.writestr('word/header1.xml', "\n".join(hdr_xml))

            ftr_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">',
                '  <w:p>',
                '    <w:pPr>',
                '      <w:pBdr>',
                '        <w:top w:val="single" w:sz="4" w:space="4" w:color="CCCCCC"/>',
                '      </w:pBdr>',
                '      <w:tabs>',
                '        <w:tab w:val="right" w:pos="9746"/>',
                '      </w:tabs>',
                '    </w:pPr>',
                '    <w:r>',
                '      <w:rPr>',
                '        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>',
                '        <w:sz w:val="18"/>',
                '        <w:color w:val="444444"/>',
                '      </w:rPr>',
                '      <w:t>Dept. of CSE, KIT Kanpur</w:t>',
                '    </w:r>',
                '    <w:r>',
                '      <w:tab/>',
                '    </w:r>',
                '    <w:fldSimple w:instr="PAGE">',
                '      <w:r>',
                '        <w:rPr>',
                '          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>',
                '          <w:sz w:val="18"/>',
                '          <w:color w:val="444444"/>',
                '        </w:rPr>',
                '        <w:t>1</w:t>',
                '      </w:r>',
                '    </w:fldSimple>',
                '  </w:p>',
                '</w:ftr>'
            ]
            z.writestr('word/footer1.xml', "\n".join(ftr_xml))

            styles_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">',
                '  <w:docDefaults>',
                '    <w:rPrDefault>',
                '      <w:rPr>',
                '        <w:rFonts w:ascii="Times New Roman" w:eastAsia="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>',
                '        <w:sz w:val="22"/>',
                '        <w:lang w:val="en-US"/>',
                '      </w:rPr>',
                '    </w:rPrDefault>',
                '  </w:docDefaults>',
                '</w:styles>'
            ]
            z.writestr('word/styles.xml', "\n".join(styles_xml))

            doc_xml = [
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"',
                '            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"',
                '            xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"',
                '            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"',
                '            xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">',
                '  <w:body>'
            ]
            doc_xml.extend(self.body_xml)

            doc_xml.append('''
    <w:sectPr>
      <w:headerReference w:type="default" r:id="rIdHeader1"/>
      <w:footerReference w:type="default" r:id="rIdFooter1"/>
      <w:titlePg/>
      <w:pgSz w:w="11906" w:h="16838" w:code="9"/>
      <w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" w:header="720" w:footer="720" w:gutter="0"/>
      <w:cols w:space="720"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>''')
            full_doc_str = "\n".join(doc_xml)
            ET.fromstring(full_doc_str)
            z.writestr('word/document.xml', full_doc_str)

        print(f"SUCCESS! {output_path} generated ({len(open(output_path, 'rb').read())} bytes).")


def build_complete_docx():
    builder = DocxBuilder()

    # COVER PAGE
    builder.add_p("Dr. A.P.J. Abdul Kalam Technical University, Lucknow", align="center", bold=True, size=21, color="555555", space_before=200, space_after=300)

    builder.add_p("“SarkariPedia: Automated Directory, Web Crawler, and", align="center", bold=True, size=31, color="0D1B2A", space_before=100, space_after=60)
    builder.add_p("Real-Time Health-Monitoring Search Engine for Indian", align="center", bold=True, size=31, color="0D1B2A", space_before=0, space_after=60)
    builder.add_p("Government Portals”", align="center", bold=True, size=31, color="0D1B2A", space_before=0, space_after=360)

    builder.add_p("A Mini Project Report Submitted in Partial Fulfillment of the Requirements for the", align="center", italic=False, size=22, color="333333", space_before=100, space_after=60)
    builder.add_p("Degree of", align="center", italic=False, size=22, color="333333", space_before=0, space_after=120)

    builder.add_p("Bachelor of Technology", align="center", bold=True, size=28, color="1B263B", space_before=60, space_after=60)
    builder.add_p("in", align="center", italic=False, size=22, color="333333", space_before=0, space_after=60)
    builder.add_p("Computer Science & Engineering", align="center", bold=True, size=26, color="1B263B", space_before=0, space_after=240)

    builder.add_p("Submitted By:", align="center", bold=True, size=22, color="1B263B", space_before=60, space_after=120)

    headers = ["S.No.", "Student Name", "Roll Number", "Branch and Section"]
    rows = [["1", "____________________", "____________________", "CSE"]]
    builder.add_table(headers, rows, col_widths=[1000, 3600, 3146, 2000])

    builder.add_p("Under the Supervision of:", align="center", bold=True, size=22, color="1B263B", space_before=180, space_after=40)
    builder.add_p("Mr./Ms. ____________________ (Assistant Professor)", align="center", bold=True, size=23, color="0D1B2A", space_before=0, space_after=300)

    builder.add_p("Department of Computer Science & Engineering", align="center", bold=True, size=23, color="0D1B2A", space_before=0, space_after=40)
    builder.add_p("Kanpur Institute of Technology, Kanpur", align="center", bold=True, size=25, color="C9630A", space_before=0, space_after=40)
    builder.add_p("Dr. A.P.J. Abdul Kalam Technical University, Lucknow", align="center", italic=False, size=21, color="555555", space_before=0, space_after=40)
    builder.add_p("Academic Session: 2026–2027", align="center", bold=True, size=21, color="333333", space_before=40, space_after=200)

    builder.add_page_break()

    with open(MD_FILE) as f:
        text = f.read()

    parts = text.split('<div style="page-break-after: always;"></div>')

    fig_map = {
        "1.3.1": ("fig_1_3_1.png", "Fig. 1.3.1: Structural pipeline and data flow of SarkariPedia"),
        "1.4.1": ("fig_1_4_1.png", "Fig. 1.4.1: Agile lifecycle model followed in the project"),
        "1.4.2": ("fig_1_4_2.png", "Fig. 1.4.2: Crawler and classification flow chart"),
        "2.3.1": ("fig_2_3_1.png", "Fig. 2.3.1: Deployment architecture and container model"),
        "3.1.2.1": ("fig_3_1_2_1.png", "Fig. 3.1.2.1: Requirement engineering cycle"),
        "4.1.1": ("fig_4_1_1.png", "Fig. 4.1.1: Layered system architecture"),
        "4.3.1": ("fig_4_3_2.png", "Fig. 4.3.2: ER diagram of the proposed database"),
        "4.3.2": ("fig_4_3_2.png", "Fig. 4.3.2: ER diagram of the proposed database"),
        "4.4.1": ("fig_4_4_1.png", "Fig. 4.4.1: Level 0 Data Flow Diagram (DFD)"),
        "4.4.2": ("fig_4_4_2.png", "Fig. 4.4.2: Level 1 Data Flow Diagram (DFD)"),
        "4.5.1": ("fig_4_5_1.png", "Fig. 4.5.1: Use Case Diagram for Citizen and Admin actors"),
        "4.6.1": ("fig_4_6_1.png", "Fig. 4.6.1: Heuristic classification decision tree"),
        "5.5.1": ("fig_5_5_1.png", "Fig. 5.5.1: Illustrative sample website interface (schematic)"),
        "5.6.1": ("fig_5_6_1.png", "Fig. 5.6.1: Planned implementation schedule"),
        "6.2.1": ("fig_6_2_1.png", "Fig. 6.2.1: Agile testing cycle"),
    }

    def parse_section(sec_text):
        lines = sec_text.split('\n')
        i = 0
        in_code = False
        code_lines = []
        in_table = False
        table_lines = []

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            if stripped.startswith('```'):
                if in_code:
                    in_code = False
                    is_ascii_art = any("+---" in cl or "| [Header]" in cl for cl in code_lines)
                    if not is_ascii_art:
                        builder.add_code_block(code_lines)
                    code_lines = []
                else:
                    in_code = True
                    code_lines = []
                i += 1
                continue

            if in_code:
                code_lines.append(line)
                i += 1
                continue

            if stripped.startswith('|') and stripped.endswith('|'):
                table_lines.append(stripped)
                i += 1
                continue
            elif table_lines:
                headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                rows = []
                for tl in table_lines[2:]:
                    row = [c.strip() for c in tl.split('|')[1:-1]]
                    if row:
                        rows.append(row)
                builder.add_table(headers, rows)
                table_lines = []

            if not stripped or stripped == '---' or stripped.startswith('<br') or stripped.startswith('<div'):
                i += 1
                continue

            if stripped.startswith('# CHAPTER') or stripped == '# REFERENCES':
                builder.add_h1(stripped.lstrip('#').strip(), space_before=400, space_after=180)
                i += 1
                continue
            elif stripped.startswith('## '):
                builder.add_h2(stripped[3:].strip(), space_before=240, space_after=100)
                i += 1
                continue
            elif stripped.startswith('### '):
                builder.add_h3(stripped[4:].strip(), space_before=180, space_after=70)
                i += 1
                continue

            m_fig = re.search(r'\*\*Fig\.\s*([\d\.]+):?\s*(.*?)\*\*', stripped)
            if m_fig:
                fig_num = m_fig.group(1).rstrip(':')
                fig_title = m_fig.group(2).strip()
                if fig_num in fig_map:
                    fn, default_cap = fig_map[fig_num]
                    cap = f"Fig. {fig_num}: {fig_title}" if fig_title else default_cap
                    builder.add_image(fn, cap)
                    if fig_num == "5.5.1":
                        builder.add_callout("[LIVE: 200 OK]  UIDAI Aadhaar Portal  |  https://uidai.gov.in  |  Citizen Services  |  Checked: 2026-11-08")
                        builder.add_p("The line above shows the form in which a verified portal entry appears in directory search results and API responses.", italic=True, size=19, space_after=160)
                i += 1
                continue

            if stripped.startswith('* ') or stripped.startswith('- '):
                bullet_body = stripped[2:].strip()
                m_b = re.match(r'\*\*(.*?)\*\*:?\s*(.*)', bullet_body)
                if m_b:
                    builder.add_bullet(m_b.group(2).strip(), bold_prefix=m_b.group(1).strip() + ":")
                else:
                    builder.add_bullet(bullet_body)
                i += 1
                continue

            clean_text = stripped.replace('**', '').replace('*', '').replace('`', '')
            builder.add_p(clean_text)
            i += 1

        if table_lines:
            headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
            rows = [[c.strip() for c in tl.split('|')[1:-1]] for tl in table_lines[2:]]
            builder.add_table(headers, rows)

    for p_idx, part in enumerate(parts[1:], 1):
        parse_section(part)
        if p_idx < len(parts) - 1:
            builder.add_page_break()

    builder.build_docx(OUT_DOCX)

if __name__ == "__main__":
    build_complete_docx()
