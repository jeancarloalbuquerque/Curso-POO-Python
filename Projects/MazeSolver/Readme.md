# Maze Solver

## Sobre

Esse projeto tem como propósito estudar os diferentes algoritmos para resolução de labirintos.

Para todo o projeto, será utilizado a ferramenta geradora de labirintos do [dcode](https://dcode.fr).

[Ferramenta geradora de labirintos](https://dcode.fr/maze-generator)

**Utilizar os seguintes critérios**

- ``'█'`` paredes;
- ``' '`` caminhos;
- ``'X'`` saída do labirinto;
- ``'O'`` ponto de início.

**Exemplo**

```
 origem
   /
  /
 V
█O███████████████████
█     █       █     █
█ ███ ███████ █ ███ █
█   █ █   █ █ █ █ █ █
█ ███████ █ █ ███ █ █
█     █         █ █ █
█ ███ ███████ █ █ █ █
█ █     █     █     █
█ █████████████ █ ███
█     █       █ █   █
███ █ █ ███ █ ███ █ █
█   █ █   █ █ █ █ █ █
█████ █ ███████ ███ █
█   █ █ █     █   █ █
█ █ █ █ █ ███ █ ███ █
█ █ █ █ █ █ █   █   █
█ ███ █ █ █ █████ ███
█   █               █
█ █ █ ███ ███████ █ █
█ █     █       █ █ █
███████████████████X█
                   ^
                  /
                 /
              saída
```