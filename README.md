# JI Auth

Canvas token and JOJ SID are within reach in CLI.

## Getting Started

### Install

```bash
$ pip3 install ji-auth
$ ji-auth --help
Usage: __main__.py [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show version.
  --help     Show this message and exit.

Commands:
  canvas  Get a newly generated token from Canvas.
  joj     Get the SID from JOJ cookies.
```

### Example

```bash
$ ji-auth canvas

    :;;
    *%%:                                :;
    ?%%                                 *?:
    %%?                                 ;;
   :%%*
   :%%+       :+?**;       :+*+;:+;    :+;      :+?%??:
   +%%;      *%?**??;     ;%%**%?%*    ;%+     +%%%%%%*
   *%%:     +%+   :%?    :??:  :*%*    +%:    ;%%*:  ::
   ?%%     ;%?     ?%    +%+    ;%*    *%     *%%;
   %%?     *?;     *%:   ?%:    ;%*    ?%     %%%
  :%%+     %%      ?%:   ?%     :%*    %?     %%?
  :S%;     %?      %%    %%:    ;%*   :%+     %%%
  +%%:     %?     +%*    ?%;    ;%*   ;%+     %%%;
  *%%      %%:   :%?     +%*:   ?%*   +%:     +%%*:
  ?%%      ;??;;;?%;     :%?*:*%+%*   ?S       *%%%*+?*
  %%?       +%%%%*:        %%%%;;%*   ??       :*%%?%%+
              ::             :  :%*               :;:
                                ;%*
                                ;%*
                                :%*

Please enter the shown captcha: loqic
Please enter jaccount username: whoami
Please enter password:
Here is your token:
N12R8Y5lBlWRDbfA4aY585wVss4d94rcZIrfaL5uYbTvXvhEcn5gmcI90HkwBmT0
```

```bash
$ ji-auth joj

  ;+??++:      :++*+:         ;+*?*;        ;+*+;
  ;???*?:     +?*+***;       +?%??%?*      **+**?:
   ;?;       +?;   :??      *%?:  ;??+    +*;   %+
   +?:      :?*     *?     ;??;   :???   :%+    ??
   ??       +?:     *?:    ???     ???   +?+;;:;?*
   ??       ??      *%     ?%*    :???   ??*?%???+
  :?+       %?      %?    :??+    ;??+   ??
  :?+       ??     ;?;    :??*    *??    ??
  ;?;       *?     ?*      ?%?   :?%+    *?;
  ;?*;:     ;?*;:;*?;      ;??*++??+     ;??; ::;
   +??;      ;??*?*:        ;*%??*;       ;*????+
    ::          :              :             :

Please enter the shown captcha: tooe
Please enter jaccount username: whoami
Please enter password:
Here is your SID:
f81e97be727da18e388d6fa53782e00a74d907ab75e20b39973392f0fad480c6
```

## Acknowledgements
- [python-jaccount-cli](https://github.com/tc-imba/python-jaccount-cli)

