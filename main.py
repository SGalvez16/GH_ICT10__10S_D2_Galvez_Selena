# working with sets

from pyscript import display

sports = {'Adriana', 'Margo', 'Franceska', 'Michaela', 'Chris', 'Harvey'}  # first club
academics = {'Adriana', 'Margo', 'Franceska', 'Kelsey', 'Chris', 'Selena'} # second club
display(sports, target = 'output')
display(academics, target = 'output')

display(sports | academics, target = 'output') 
display(sports & academics, target = 'output') 
display(sports - academics, target = 'output')
display(academics - sports, target = 'output')
display(sports ^ academics, target = 'output')

