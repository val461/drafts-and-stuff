IRB.conf[:PROMPT][:DEFAULT] = {
  :PROMPT_I => "%N(%m)[%i]> ",  # normal prompt
  :PROMPT_S => "%N(%m)[%i]%l… ",# prompt for continuated strings
  :PROMPT_C => "%N(%m)[%i]_ ",  # prompt for continuated statement
  :RETURN => "\n=> %s\n"        # format to return value
}

IRB.conf[:PROMPT][:SIMPLE] = {
  :PROMPT_I => "> ",    # normal prompt
  :PROMPT_S => "%l… ",  # prompt for continuated strings
  :PROMPT_C => "",      # prompt for continuated statement
  :RETURN => "=> %s\n"  # format to return value
}

IRB.conf[:PROMPT_MODE] = :SIMPLE

IRB.conf[:AUTO_INDENT] = true
IRB.conf[:SAVE_HISTORY] = 20
require 'irb/completion'
