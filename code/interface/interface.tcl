#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m40" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 576x261+578+67
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "ROS Test Controller"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure Button -background #d9d9d9
    ttk::style configure Button -foreground #000000
    ttk::style configure Button -font TkDefaultFont
    button $top.but38 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Record Bag} 
    vTcl:DefineAlias "$top.but38" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Initialize 
    vTcl:DefineAlias "$top.but39" "Button2" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m40 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    message $top.mes41 \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Connection Status: Good
} -width 140 
    vTcl:DefineAlias "$top.mes41" "Message1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent47 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent47" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Participant 
    vTcl:DefineAlias "$top.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Test Number} 
    vTcl:DefineAlias "$top.lab49" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent50" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but51 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Save 
    vTcl:DefineAlias "$top.but51" "Button3" vTcl:WidgetProc "Toplevel1" 1
    message $top.mes52 \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Test Status: Waiting To Start...} -width 180 
    vTcl:DefineAlias "$top.mes52" "Message2" vTcl:WidgetProc "Toplevel1" 1
    message $top.mes53 \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Datetime: 01/25/2018 00:00} -width 168 
    vTcl:DefineAlias "$top.mes53" "Message3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but38 \
        -in $top -x 280 -y 160 -width 71 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but39 \
        -in $top -x 190 -y 160 -width 71 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes41 \
        -in $top -x 360 -y 100 -width 140 -relwidth 0 -height 23 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent47 \
        -in $top -x 140 -y 70 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 60 -y 70 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 60 -y 100 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 140 -y 100 -width 44 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 200 -y 100 -anchor nw -bordermode ignore 
    place $top.mes52 \
        -in $top -x 200 -y 210 -width 180 -relwidth 0 -height 13 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes53 \
        -in $top -x 350 -y 70 -width 168 -relwidth 0 -height 23 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37
