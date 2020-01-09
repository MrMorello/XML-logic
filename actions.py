def f_set(action="", label=" "):
    return "<action name=\"{}\">\n\
                <params>\
                    <param name=\"data\">result={}::str</param>\
                </params>\
            </action>".format(action, label)

print(f_set("set", "label"))