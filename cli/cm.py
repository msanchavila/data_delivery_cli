import click


@click.group('cm')
def cm_group():
    '''Create College Match delivery spreadsheets

    Args:

    \b
        --parsing <File>: Parsing sheet for students
    '''

@cm_group.command('load_data')
@click.argument('data_dir', type=click.Path(exists=True))
def load_student_data():
    '''Load Student data into database'''
    pass


@cm_group.command('load_parsing')
@click.argument('parsing_sheet', type=click.File('rb'))
@click.argument('phase', type=click.Choice(['Rank', 'RevRank', 'Match', 'RD']))
def load_parsing_file():
    '''Load parsing file into database

    \b
    phase: Rank|RevRank|Match|RD
    '''
    pass


@cm_group.command('generate')
@click.option('--slate',is_flag=True, help='Only create Slate deliverables')
@click.option('--questvm',is_flag=True, help='Only create QuestVM deliverables')
@click.option('--population', type=click.Choice(['F', 'NF', 'NP']), 
              help='Choice of student populations to export')
def create_deliverables(slate, questvm, population):
    '''Create deliverables'''
    pass