# ----------------------------------------------------------------------------
"""
  Basilic library
  
  Essential library for divers tools... 
    
  Author: Rémi Mignot, 2020.
"""

import os, sys


# ------------------------------------------------------------------------------
def f_clc():
  """ 
    CLear Command window
    
    Clear the screen (to use in a script or function). 
    -> as cls (windows), clc (Matlab), or clear (UNIX).  
    
    usage: 
    >>> f_clc()
  """  
  os.system( 'cls' if os.name=='nt' else 'clear' )
#.enddef 'f_clc'


# ------------------------------------------------------------------------------
def f_oos( inString_k, n = 0 ):
  """ 
    Out Of Spaces 
      
    Remove the indentation spaces of each lines of the input string, 
    or replace them with n spaces. 
    This function is useful when defining a string with multiple lines using 
    the triple double quotes, and respecting the code identation. 
    
    usage:
     >>> outString_k = f_oos( inString_k [, n ] )
    
    The argument "n" is the number of spaces to add before each line. 
  """
  
  # Replace tabulations by single spaces, in the input string
  inString_k = inString_k.replace( '\t', ' ' )    

  # Copy to a temporary string, and add a return at the beginning and the end... 
  tmp_k = '\n' + inString_k + '\n'

  # Remove empty lines , which are problematic... 
  patt_k = '\n'  
  while tmp_k.count( patt_k ) >= 1:  
    while tmp_k.count( patt_k + '\n' ) >= 1:
      tmp_k = tmp_k.replace( patt_k + '\n', '\n' )    
    patt_k = patt_k + ' '

  # and remove the last return
  if tmp_k[-1] == '\n': tmp_k = tmp_k[0:-1]    

  # Search the number of space to remove (or to replace)
  patt_k = '\n'
  while ( tmp_k.count( patt_k ) - tmp_k.count( patt_k + ' ' )  ) <= 0: 
    patt_k = patt_k + ' '

  # Add a return at the beginning if needed
  no_start_return = False
  if inString_k[0] != '\n': 
    inString_k = '\n' + inString_k
    no_start_return = True
  
  # New number of string, if any... 
  new_patt_k = '\n' + ' ' * n
  
  # Replace the beginning of the lines
  outString_k = inString_k.replace( patt_k, new_patt_k )
    
  # Remove the added return if any
  if no_space_0: outString_k = outString_k[1:]
  
  # Remove the last spaces after the last return
  ilastspace = out_k.rfind( '\n' )
  out_k = out_k[0:ilastspace+1]
  
  return outString_k
#.enddef f_oos


# ------------------------------------------------------------------------------
#def f_system( command_k, excep_b = False ):
  """
    call System command
    
    Call the input system command, and return the output string, and 
    the success status. 
    
    usage:
      >>> [status, stdout_k, stderr_k] = f_system( command_k, excep_b=False )
    
    excep_b: 
      If excep_b is True, an exception is raised if the command fails, 
      if excep_b is False, in case the command fails, the function is 
      terminated by returning status = 1.     
    
    stdout_k:
      output string returned in stdout, 
      
    stderr_k:
      output string returned in stderr, 
  """
  
  
#.endif f_system


# ------------------------------------------------------------------------------
def f_get_startup_code( post_name_k = '', get_number_b = False ):  
  """ 
    Get the Startup Code
    
    Return the concatenated code source of startup script(s) to be executed 
    by exec() at startup. 
    
    The first executed script is './startup' + post_name_k + '.py', 
    then the scripts '.py' contained in the folder './startup' + post_name_k, 
    in the alphabetical order. 
    
    The startup script(s) can be used to initialise some variables or 
    modules related to your project. 
        
    usage: 
      >>> import basilic
      >>> exec( basilic.f_get_startup_code( post_name_k ) )
      
    If the argument get_number_b is True, the number of found scripts is returned. 
    usage: 
      >>> startup_code_k, n_scripts \
      ...   = basilic.f_get_startup_code( post_name_k, get_number_b = True )
  """
  
  # Init the string to be executed and number of found scripts 
  startup_string = '';
  n_scripts = 0
  
  # 1) get startup?.py
  startup_script_file = './startup' + post_name_k + '.py' 
  if os.path.isfile( startup_script_file ):
    startup_string += open( startup_script_file ).read() + '\n'
    n_scripts += 1
  
  # 2) run the *.py scripts contained in ./startup?.d/, in alphabetical order, 
  startup_script_dir = './startup' + post_name_k + '.d/' 
  if os.path.isdir( startup_script_dir ):
    for __script_tmp in sorted(  os.listdir( startup_script_dir )   ):
      if __script_tmp.endswith( '.py' ):
        startup_string += open( startup_script_dir + __script_tmp ).read()  + '\n'
        n_scripts += 1
  #.endif
  
  # Return the concatenated commands
  if get_number_b:
    return startup_string, n_scripts
  else:
    return startup_string
  
#.enddef 'f_get_startup_code'


# --------------------------------------------------------------------------
# To execute during import

# Check the platform
if sys.platform != 'linux':
  warning_messages = 'WARNING: basilic has been developped and tested with GNU/Linux only.'
  print( '\033[91m' + warning_messages + '\033[0m'  )
#.endif 
