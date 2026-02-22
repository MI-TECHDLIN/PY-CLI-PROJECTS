import json
# jsonhandler
class jsonfile:
      def loadfile(self):
            try:
                  with open(self,'r') as self:
                        return json.load(self)
            except FileNotFoundError,json.JSONDecodeError:
                  return['file not found']
            
      def savefile(self,file):
            with open(file,'w') as file:
                  return json.dump(self,file,indent=1)
       
