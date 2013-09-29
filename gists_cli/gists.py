#!/usr/bin/env python

import sys, actions, log, util

#-------------------------------------------

def main ( ):

  args = sys.argv
  
  print ''

  if len(args) == 1:
    log.comment ("No arguments specified, listing your Gists. Try '%s help' if you need help." % sys.argv[0])
    print ''

  log.debug ("Arguments " + str( args ))

  del args[0] # Delete the filename
  cmd = None

  """---------------------------------------
  default command if no arguments at all
    list
  """
  if len(args) == 0:
    actions.list()
  else:
    """---------------------------------------
    If args > 1, args[0] is the command. We remove it from the list
    args now contains only the  command arguments
    """
    cmd = args[0]
    del args[0] # Delete the command. Arguments remaining are the options for each command
    log.debug ("Potential cmd: " + cmd)
    log.debug ("Adjusted arguments " + str( args ))

    """ ---------------------------------------
    cmd args = 0:
      create
      ID
      token|t
    """
    if len(args) == 0:
      if cmd in ("new", "n", "create", "c"):
        actions.create()  # Create with no args
      elif cmd in ("token", "t"):
        actions.updateCredentials()
      else:
        actions.view( cmd )  # if there are no args and the cmd doesnt match, assume the cmd is the gist id
    else:
      """ -----------------------------------------
      cmd args = 1+:
         create CONTENT
         create FILE
         create private
         create private CONTENT
         create private FILE
         append ID
         update ID
         delete ID
         ID path
      """
      if cmd in ("new", "n", "create", "c"):
        if len(args) == 1:
          # check if the arg is a Boolean, File or Content
          if util.parseBool(args[0]) != None:
            actions.create( public = util.parseBool(args[0]) )
          elif util.isFile(args[0]) == True:
            actions.create( filename = args[0] )
          else:
            actions.create( content = args[0] )
        elif len(args) > 1: 
          # args could be boolean and File, or Boolean and Content
          actions.create( )
      elif cmd in ("append", "a"):
        actions.append( args[0] )
      elif cmd in ("update", "u"):
        actions.update( args[0] )
      elif cmd in ("delete", "d"):
        actions.delete( args[0] )
      else:
        # No match = get
        actions.get( cmd, args[0] ) # if no match, cmd has the ID, arg[0] has the path

  log.debug ("Done.")
  print ''

#-------------------------------------------

if __name__ == "__main__":
  main ()

#-------------------------------------------