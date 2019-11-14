## **i3_meta_workspaces**

This code enables multiple meta workspaces within your i3 window manager. It is very useful when working in multiple projects. 
`$mod+X` usually allows you to access different workspaces. This script allows you to shift between different collections of workspaces i.e. meta workspaces. 

## **Usage**

Shift to meta workspace number X with:

`$mod+Control+X`

You can then use navigate to different windows with:

`$mod+X`

And move windows within the meta workspace with:

`$mod+Shift+X`

## **Installation**

1. Place *meta_workspaces.py* in the *~/.config/i3/* folder.
2. Modify your i3 config to the following:

```c
set $script_path ~/.config/i3/meta_workspaces.py

# change to workspace
bindsym $mod+1 exec "python3 $script_path -w 1"
bindsym $mod+2 exec "python3 $script_path -w 2"
bindsym $mod+3 exec "python3 $script_path -w 3"
bindsym $mod+4 exec "python3 $script_path -w 4"
bindsym $mod+5 exec "python3 $script_path -w 5"
bindsym $mod+6 exec "python3 $script_path -w 6"
bindsym $mod+7 exec "python3 $script_path -w 7"
bindsym $mod+8 exec "python3 $script_path -w 8"
bindsym $mod+9 exec "python3 $script_path -w 9"
bindsym $mod+0 exec "python3 $script_path -w 0"

# move focused container to workspace
bindsym $mod+Shift+1 exec "python3 $script_path -mw 1"
bindsym $mod+Shift+2 exec "python3 $script_path -mw 2"
bindsym $mod+Shift+3 exec "python3 $script_path -mw 3"
bindsym $mod+Shift+4 exec "python3 $script_path -mw 4"
bindsym $mod+Shift+5 exec "python3 $script_path -mw 5"
bindsym $mod+Shift+6 exec "python3 $script_path -mw 6"
bindsym $mod+Shift+7 exec "python3 $script_path -mw 7"
bindsym $mod+Shift+8 exec "python3 $script_path -mw 8"
bindsym $mod+Shift+9 exec "python3 $script_path -mw 9"

# change meta workspace
bindsym $mod+Control+1 exec "python3 $script_path -m 1"
bindsym $mod+Control+2 exec "python3 $script_path -m 2"
bindsym $mod+Control+3 exec "python3 $script_path -m 3"
bindsym $mod+Control+4 exec "python3 $script_path -m 4"
bindsym $mod+Control+5 exec "python3 $script_path -m 5"
bindsym $mod+Control+6 exec "python3 $script_path -m 6"
bindsym $mod+Control+7 exec "python3 $script_path -m 7"
bindsym $mod+Control+8 exec "python3 $script_path -m 8"
bindsym $mod+Control+9 exec "python3 $script_path -m 9"
bindsym $mod+Control+0 exec "python3 $script_path -m 0"
```
