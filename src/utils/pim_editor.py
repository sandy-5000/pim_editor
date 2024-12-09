import sys
import curses
from .editor_state import EditorState
from .file_handler import open_file


def normal_mode(key, state):

    if state.command == '' and key == ord('i'):
        state.mode = 'INSERT'
    # elif command == '' and key == ord('p'):
    #     paste_from_clipboard()
    elif key in (curses.KEY_BACKSPACE, 127, 8):
        if state.command:
            state.command = state.command[0:len(state.command) - 1]
    elif key in (curses.KEY_ENTER, 10):
        state.command = state.command.strip()
        if state.command == ':q':
            return False
        # elif command == ':w':
        #     save_file()
        elif state.command == ':r':
            open_file()
        elif state.command.startswith(':set '):
            r = state.command[5:]
            if r == 'nu':
                state.show_line_numbers = True
        elif state.command.startswith(':unset '):
            r = state.command[7:]
            if r == 'nu':
                state.show_line_numbers = False
        elif state.command.startswith(':y'):
            r = state.command[2:].split(',')
            if len(r) != 2:
                state.message = 'Invalid positions'
            # else:
            #     copy_to_clipboard(r[0].strip(), r[1].strip())
        else:
            state.message = 'Invalid command'
        state.command = ''
    elif key == ord(':'):
        state.command = ':'
    elif state.command and state.command[0] == ':':
        state.command = state.command + chr(key)
    return True


def pim_editor(stdscr, file_name):
    curses.curs_set(1)

    text, error = open_file(file_name)
    if error != None:
        print('Error: coundn\'t read File: {file_name}')
        sys.exit(1)

    state = EditorState(stdscr)
    state.mode = 'NORMAL'
    state.text = text
    state.number_bar_width = len(str(len(text))) + 1
    state.view_y = 0
    state.set_cursor_x(0)
    state.set_cursor_y(0)
    state.file_name = file_name

    while True:

        state.refresh()
        key = stdscr.getch()

        if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            state.move_cursor(key)
            continue
        if state.mode == 'NORMAL':
            if not normal_mode(key, state):
                break
        elif state.mode == 'INSERT':
            if key == 27: # Esc
                state.mode = 'NORMAL'
                continue
            elif key in (curses.KEY_BACKSPACE, 127, 8):  # Backspace
                # handle_backspace()
                pass
            elif key in (curses.KEY_ENTER, 10):  # Enter
                # handle_enter()
                pass
            else:
                # handle_all_keys(key)
                pass