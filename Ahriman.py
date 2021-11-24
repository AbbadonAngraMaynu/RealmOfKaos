"""Controlla e lancia tutti gli altri script da linea di comando"""

import sys

import cmd
# import pyreadline
import yaml


class Ahriman(cmd.Cmd):
    intro = "I am Ahriman, master of the forbidden library. Ask your question, but beware: you may not" \
            "be pleased with the answer."
    prompt = "(Ahriman)$:"

    completekey = None

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.config_data = self.load_configuration("config.yaml")

    def do_awake_dagon(self, t):
        """Runs the Dagon Script"""
        print(t)
        print("Dagon is sleeping, perform the ritual")

    def do_awake_migo(self, file):
        """Runs the MiGo Script"""
        print("Dagon is sleeping, perform the ritual")

    def do_create_structure(self, arg):
        """Crea la struttura di cartelle necessaria per gli script"""

    def do_reconfig(self, filename):
        """Ricarica le configurazioni"""
        self.config_data = self.load_configuration(filename)

    def do_printconfig(self, arg):
        """Print the configuration data [raw]"""
        print(yaml.dump(self.config_data))

    def do_bye(self, arg):
        """Quit the shell"""
        print('(Ahriman)$: Begone')
        return True

    # """Funzioni di aiuto interne"""
    def load_configuration(self, file):
        return yaml.safe_load(open(file))


if __name__ == "__main__":
    a = Ahriman()
    a.cmdloop()
    sys.exit(0)
