<p align='center'>
<img src='../_images/logo.png' width='512px'/>
</p>

# Hooks

The hook function can only be defined in the Applet class. It is a function actively called by the system at a certain moment. It allows users to capture events triggered by the system through the hook function.

- \_\_kill\_\_(self)
  - The hook is triggered when the applet is terminated, and the user releases resources here, such as: thread
- OnContextMenuHook(self,[m](../_modules/XiR/hook/ContextMenuEvent.md))
  - The hook function is triggered when the user clicks on the context menu
