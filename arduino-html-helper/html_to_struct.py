from html.parser import HTMLParser



class MyHTMLparser(HTMLParser):
    structhead_printed = False
    formparserhead_printed = False
    str_eeprom = ""
    str_formparser = ""

    def nexttag_to_eeprom(self, tag, attrs):

        if self.structhead_printed == False:
            self.structhead_printed = True
            self.str_eeprom = "struct program {"

        hsh = {}
        for item in attrs:
            hsh[item[0]] = item[1]

        self.str_eeprom += '\n\n\\\\\t' + str(hsh)

        if hsh['type'] == "number":
            self.str_eeprom += "\n\tint " + hsh['name'] + ";"

        if hsh['type'] == "text":
            if "maxlength" in hsh.keys():
                self.str_eeprom += "\n\tchar " + hsh['name'] + "[" + hsh['maxlength'] + "];"
            else:
                self.str_eeprom += "\n\tchar " + hsh['name'] + "[MAXTEXTLEN];"

        if hsh['type'] == "time":
            self.str_eeprom += "\n\tint " + hsh['name'] + "hh;"
            self.str_eeprom += "\n\tint " + hsh['name'] + "mm;"

        if hsh['type'] == "checkbox":
            self.str_eeprom += "\n\tboolean " + hsh['name'] + ";"

    def nexttag_to_form(self, tag, attrs):

        if self.formparserhead_printed == False:
            self.formparserhead_printed = True
            self.str_formparser = "void handleset()"
            self.str_formparser += "\n{"

        hsh = {}
        for item in attrs:
            hsh[item[0]] = item[1]
        #print("//", hsh)

        if hsh['type'] == 'reset':
            return

        if hsh['type'] == 'submit':
            return

        if hsh['type'] == 'button':
            return

        mydict[hsh['name']] = 'myeprom.prg[pid].' + hsh['name'] + ';'

        self.str_formparser += '\n\nif ( server.argName(i) == "' + hsh['name'] + '\" )'
        self.str_formparser += '\n { '
        if hsh['type'] == 'text':
            self.str_formparser += '\n\t s2 = (String)server.arg(i); '
            self.str_formparser += '\n\t s2.toCharArray(myeprom.prg[pid].' + hsh['name'] + ',' + hsh['maxlength'] + ');'
            self.str_formparser += '\n\t debugmsg += \"\\nprg[\"+pid+\"].\"'+ hsh['name'] + ' updated to:";'
            self.str_formparser += '\n\t debugmsg += myeprom.prg[pid].' + hsh['name'] + ';'

        if hsh['type'] == 'number':
            # print(" s2 = (String)server.arg(i); ")
            self.str_formparser += '\n\t s2 = (String)server.arg(i); '
            self.str_formparser += '\n\t myeprom.prg[pid].' + hsh['name'] + ' = s2.toInt();'
            self.str_formparser += '\n\t debugmsg += \"\\nprg[\"+pid+\"].\"'+ hsh['name'] + ' updated to:";'
            self.str_formparser += '\n\t debugmsg += myeprom.prg[pid].' + hsh['name'] + ';'

        if hsh['type'] == 'checkbox':
            self.str_formparser += '\n\t s2 = (String)server.arg(i); '
            self.str_formparser += '\n\t myeprom.prg[pid].'+ hsh['name'] + ' = s2.toInt();'
            self.str_formparser += '\n\t debugmsg += \"\\nprg[\"+pid+\"].\"'+ hsh['name'] + ' updated to:";'
            self.str_formparser += '\n\t debugmsg += myeprom.prg[pid].' + hsh['name'] + ';'

        if hsh['type'] == 'time':
            self.str_formparser += '\n\t s2 = (String)server.arg(i); '
            self.str_formparser += '\n\t myeprom.prg[pid].' + hsh['name'] + ' = s2.toInt();'
            self.str_formparser += '\n\t debugmsg += \"\\nprg[\"+pid+\"].\"'+ hsh['name'] + ' updated to:";'
            self.str_formparser += '\n\t debugmsg += myeprom.prg[pid].' + hsh['name'] + ';'

        self.str_formparser += '\n } '

    def handle_inputtag(self, tag, attrs):
        # print("Encountered a input tag:", tag, attrs)
        self.nexttag_to_eeprom(tag, attrs)
        self.nexttag_to_form(tag, attrs)

    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        if (tag == "input"):
            self.handle_inputtag(tag, attrs)

    def handle_endtag(self, tag):
        # print("Encountered an end tag :", tag)
        return

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        return

def print_form_with_values(inname,outname):
    input_file = open(inname, 'r')
    output_file = open(outname,'w+')
    for line in input_file:
        line=line.rstrip()
        line=line.replace('\"','\\\"')

        if 'input name' in line:
            for word in line.split():
                if 'name=' in word:
                    name=word.split('=')[1]
                    mydict[name]='eeprom.prg[pid].'+name
                    print(name, mydict[name])
            if 'type=\"checkbox\"' in line:
                a = 'type=\\\"number\\\" value=\"+' + mydict[name]
                line.replace('type=\\\"checkbox\\\"','type=\\\"checkbox\\\" checked')
            if 'type=\"number\"' in line:
                a='type=\\\"number\\\" value=\\\"+'+mydict[name]
                line.replace('type=\\\"number\\\"', a)
            print("\\n", line, file=output_file, end='')
        print("\\", file=output_file)
    input_file.close()
    output_file.close()


inname='/Users/andras.pulai/Downloads/locsol/program.html'
outname='/Users/andras.pulai/Downloads/locsol/program_test.html'

mydict=dict()
parser = MyHTMLparser()

file_htmlform = open(inname, "r+")
data = file_htmlform.read().replace('\n', '')
file_htmlform.close()

parser.feed(data)

print("eeprom:")
print(parser.str_eeprom)

print("formparser:")
print(parser.str_formparser)

print("helper dict")
print(mydict)

print_form_with_values(inname,outname)