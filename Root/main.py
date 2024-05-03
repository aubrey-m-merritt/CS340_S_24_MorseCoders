from organism import organism
from scientificCategory import scientificCategory
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\main.log', encoding='utf-8', level=logging.DEBUG)

def main():
    print("Welcome to our Biodiversity By Country -Ditsribution of Animals, Plants, and Natural Communities System! Please select what action you will like to take next!")
    inTheSystem = True

    while inTheSystem:
        print("\tMenu:")
        print("\t\t1) Show Taxonomic Frequency with a graph of your choice")
        print("\t\t2) Perform a calculation")
        print("\t\t3) Find a specific Catergory, Taxonomic Group, or Taxonomic Subgroup in the dataset")
        print("\t\t4) Exit the program.")
        userTask = int(input("Please choice your task: "))
        if userTask == 1:
            print("\tGraph Menu:")
            print("\t\t1) Display a histogram representation of the data.")
            print("\t\t2) Display a line plot representation of the data.")
            print("\t\t3) Display a scatter plot representation of the data.")
            print("\t\t4) Display a whisker-box plot representation of the data.")
            print("\t\t5) Display a violin plot representation of the data.")
            graphPick = int(input("Enter a choice: "))
            
            if graphPick == 1: # success!
                try: 
                    organism.histogram(scientificCategory.dataframeCSV).show()
                #
                except:
                    print("Histogram not working in main")
                    logger.debug("Histogram not working in main")
                #
            #
            elif graphPick == 2: # success!
                try:
                    organism.linePlot(scientificCategory.dataframeCSV).show()
                #
                except:
                    print("Line plot not working in main")
                    logger.debug("Line plot not working in main")
                #
            #
            elif graphPick == 3: # success!
                try:
                    scientificCategory.scatterPlot(scientificCategory.dataframeCSV).show()
                #
                except:
                    print("Scatter plot not working in main")
                    logger.debug("Scatter plot not working in main")
                #
            #
            elif graphPick == 4: # success!
                try:
                    scientificCategory.whiskerBoxPlot(scientificCategory.dataframeCSV).show()
                #
                except:
                    print("Whisker plot not working in main")
                    logger.debug("Whisker plot not working in main")
                #
            #
            elif graphPick == 5: # works but not correct
                try:
                    scientificCategory.violinPlot(scientificCategory.dataframeCSV).show()
                #
                except:
                    print("Violin plot not working in main")
                    logger.debug("Violin plot not working in main")
                #
            #
        #
        elif userTask == 2:
            print("\Calculation Menu:")
            print("\t\t1) Calculate joint probabilities.")
            print("\t\t2) Calculate std, mean, and median.")
            print("\t\t3) Calculate joint counts.")
            print("\t\t4) Calculate conditional probabilities.")
            calcPick = int(input("What calculation would you like to perform? "))
            
            if calcPick == 1: # works
                scientificCategory.calculateJointProbabilities(scientificCategory.dataframeCSV,'Taxonomic Subgroup','Taxonomic Group')
            #
            elif calcPick == 2: # in progress
                scientificCategory.calculations(scientificCategory.dataframeCSV, "Scientific Category")
            #
            elif calcPick == 3: # works
                scientificCategory.calculateJointCounts(scientificCategory.dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
            #
            elif calcPick == 4: # works
                x = scientificCategory.calculateConditionalProbabilities(scientificCategory.dataframeCSV, 'Taxonomic Subgroup', 'Taxonomic Group')
                print(x)
            #
        #
        elif userTask == 3: # works
            print("\t\t1) Find category.")
            print("\t\t2) Find taxonomic group.")
            print("\t\t3) Find taxonomic Subgroup.")
            finding = int(input("Enter what you'd like to find: "))
            
            if finding == 1:
                organism.findCategory(scientificCategory.dataframeCSV, "category")
            #
            elif finding == 2:
                organism.findCategory(scientificCategory.dataframeCSV, "taxonomicGroup")
            #
            elif finding == 3:
                organism.findCategory(scientificCategory.dataframeCSV, "taxonomicSubgroup")
            #
        #
        elif userTask == 4: # works
            print("Goodbye!")
            inTheSystem = False
        #
    #
#

if __name__ == "__main__":
    main()
