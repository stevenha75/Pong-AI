import neat

def eval_genomes(genomes, config):
    pass

def run_neat(config):
    # Load into a checkpoint w/ the following code:
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-27')
    p = neat.Population(config) # initializing population w/ config
    
    # Adding reporters to see data while running
    p.add_reporter(neat.StdOutreporter(True)) 
    stats = neat.StatisticsReporter() 
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1)) # checkpoints @ each generation
    
    winner = p.run(eval_genomes, 50)

    