from bs4 import BeautifulSoup as bs


class book:
    book_text_xml:str
    def __init__(self,book_fb2:str,parsemode:str,string_num:int):
        book_full=book_fb2
        parsemode=parsemode
        string_num=string_num

    def initialize(self,book_full,parsemode):
        book_full

    soup=bs(open("/home/rencoryf/Documents/the_catcher_in_the_rye.fb2","r").read(),"xml")

    sections=soup.find_all("section")

    header=sections[0].find("title")

    print(sections[1])
