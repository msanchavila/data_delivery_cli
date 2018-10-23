import click


@click.command('cps')
@click.option('--slate',is_flag=True, help='Only create Slate deliverables')
@click.option('--questvm',is_flag=True, help='Only create QuestVM deliverables')
@click.argument('--parsing', type=click.File('rb'))
def cps_command(slate, questvm, parsing):
    '''Create College Prep Scholar delivery spreadsheets

    Args:

    \b
        --parsing <File>: Parsing sheet for students
    '''
    pass