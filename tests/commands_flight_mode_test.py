from communications.command_definitions import CommandDefinitions
from utils.constants import FMEnum, BootCommandEnum, RestartCommandEnum, NormalCommandEnum, LowBatterySafetyCommandEnum, \
    SafetyCommandEnum, OpNavCommandEnum, ManeuverCommandEnum, SensorsCommandEnum, CommsCommandEnum, TestCommandEnum, \
    CommandCommandEnum

command_enums = [BootCommandEnum, RestartCommandEnum, NormalCommandEnum, LowBatterySafetyCommandEnum,
                 SafetyCommandEnum, OpNavCommandEnum, ManeuverCommandEnum, SensorsCommandEnum, TestCommandEnum,
                 CommsCommandEnum, CommandCommandEnum, TestCommandEnum, CommandCommandEnum]


def testFlightCommands():
    cd = CommandDefinitions(None)
    all_modes = list(map(int, FMEnum))

    zipped_enums_command_dicts = list(zip(command_enums, cd.COMMAND_DICT.values()))
    # want to make sure that all command IDs defined in utils.constants matches what's in command_definitions

    error_msg = ""

    for enum, command_dict in zipped_enums_command_dicts:
        all_enum_commands = list(map(int, enum))
        all_command_ids = list(command_dict.keys())
        all_enum_commands = sorted(all_enum_commands)
        all_command_ids = sorted(all_command_ids)

        try:
            assert all_enum_commands == all_command_ids
        except AssertionError:
            commands_not_in_both = set(all_enum_commands).symmetric_difference(all_command_ids)
            error_msg += f"Commands defined in {enum} not consistent with utils.constants: {commands_not_in_both}\n"

    if error_msg != "":
        raise AssertionError(error_msg)


if __name__ == '__main__':
    testFlightCommands()
