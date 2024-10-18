# SWE_CAP1_Dzo_Spell_Checker

##Project overview 
In this project it create a straightforward command-line tool that checks spelling in Dzongkha text files. It matches words from the input file with a predefined dictionary of correct Dzongkha words and flags any errors, indicating where they occur. The tool is a step toward improving Dzongkha language tools and ensuring better accuracy in written texts.Additionally, the Dzongkha Spell Checker can help users learn and practice correct spelling in Dzongkha, making it a valuable resource for language learners, educators, and content creators. It can also be easily expanded with new words, making it adaptable to the evolving language. This tool contributes to the broader effort of supporting Dzongkha’s digital presence and promoting linguistic accuracy in official and personal writing.

##Table of contant

- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Data Structure](#data-structure)
- [Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [References](#references)

##Usage
I used python3

python SWE_CAP1_Dzo_Spell_Checker.py 339.docx 339.txt

##Implementation
Initially, the raw dictionary text file containing incorrect Dzongkha spellings has been processed to remove errors.

The code responsible for this cleaning process is located in the “cleaning_dictionary.py” file. This Python script converts a .docx file into a plain text .txt file by extracting text from each paragraph and saving it into the text file.

The Dzongkha Spell Checker project employs an algorithm that utilizes a sliding window technique to identify compound words within the text. It examines individual words or groups of words against the dictionary, flagging any word that is not found as a spelling error.

##Data structer
Data Structures

	1.	Set:
	•	Purpose: Contains valid words from the dictionary.
	•	Functionality: Offers fast membership testing, allowing for quick checks to determine if a word is correctly spelled.
	2.	List:
	•	Purpose: Used to read the input file line by line.
	•	Functionality: Stores each line of text, which can then be processed to identify individual words.
	3.	List of Tuples:
	•	Purpose: Maintains a collection of words identified as spelling errors.
	•	Functionality: Each tuple may contain information about the misspelled word and its location (e.g., line number and position), providing structured data for reporting errors.

Summary

These data structures work together to efficiently process the input text, check for spelling errors, and store results for easy retrieval and display. The use of a set ensures quick lookups, while lists facilitate straightforward file reading and error tracking.

##Algorithms
Dictionary Lookup:

The tool keeps a collection of valid Dzongkha words in a set, which allows for rapid word retrieval. While processing the input text, it verifies each word or group of words against this set. Because set lookups are highly efficient, this significantly speeds up the overall process.

Sliding Window:

Some Dzongkha words are compound words formed from two or more smaller words. To detect these valid compound words, the sliding window algorithm is employed. This algorithm begins by examining a single word and then progressively adds subsequent words to create possible compound word combinations. If a compound word is found in the dictionary, the tool recognizes it as valid and continues with the next words.

word cleaning:

Before comparing words to the dictionary, the tool strips away certain characters, such as quotation marks used in Dzongkha, that are not part of the actual words. This step ensures that the matching process is accurate and that only relevant characters are considered.This cleaning process is crucial for improving the accuracy of the spell checker, as it reduces the likelihood of false positives. By focusing solely on the core elements of each word, the tool can effectively identify spelling errors without being misled by extraneous characters. This step ultimately enhances the reliability of the overall spell-checking process.

##Performance analysis
Performance Analysis

A number of key performance metrics can form the basis for evaluating the performance of the Dzongkha Spell Checker: efficiency, accuracy, and scalability.

1.Efficiency:
Time Complexity: The use of a set to store valid words allows the average time complexity of lookups to be O(1). This makes the checking of every word against the dictionary fast, hence making the processing of the input text faster.
• Sliding Window Algorithm: The sliding window technique for compound word identification will have the tool efficiently combine smaller words into potential valid compounds. This greatly reduces the number of checks that need to be made against the dictionary, further improving the speed.

2. Accuracy:
•  Error Detection: Word cleaning removes any extraneous characters that may interfere with word matching and resulted in some false positives. With this, the tool would then use a dictionary to identify spelling errors precisely to provide good feedback to the users.
•  Handling of Compound Words: The sliding window approach to effectively recognize compound words increases the spell checker's accuracy to identify valid words. Thus, it reduces the chances of overlooking the correctly spelled terms.

4. Scalability:
• Dictionary Size: The system is able to support a large dictionary of valid Dzongkha words with no significant degradation in its performance. As the number of words goes on increasing, the set-based structure allows for real quick lookups.
• Input File Size: The spell checker works well with various sizes of input files, ranging from small documents to somewhat longer texts, while maintaining its performance since it processes documents line by line efficiently.

Overall, this spell checker of Dzongkha has very good performance characteristics efficiently balancing efficiency, accuracy, and scalability. The appropriate application of data structures and algorithms solves the user's problem of needing reliable spell-checking in Dzongkha language texts. Performance could be regularly tested and optimized for further improvement.

##Challenge and solution 
Many of the words in Dzongkha are long, wherein small words are joined together. So a sliding window approach was done in order to identify these compound words efficiently. Also, many characters and punctuation in the Dzongkha language needed to be handled, so the code removes certain symbols (like \":\") from the dictionary before matching with text files.
Character Normalization: Sometimes, the program may have a step for normalizing characters, so that different punctuation or different ways of writing the diacritics do not impede word recognition.
• Comprehensive Preprocessing: Besides the removal of some symbols, preprocessing may also involve converting all words to lowercase forms, which would further improve the uniformity and correctness of the matching.
• Formation of Compound Word: Sliding window technique allows the tool to assess dynamically the combination of words. Hence, it becomes more appropriate for finding valid compound words within the Dzongkha text.
• Improved User Experience: The spell checker, on account of better processing of characters and punctuation, consequently improves user experience by reducing false positives and providing more realistic feedback regarding spelling errors.

##Future improvments

1. Dictionary Expansion:
• Update the dictionary in a rolling manner to include words that are being invented as the Dzongkha language is developing. It can be community-driven or crowdsourced, considering the viability for such projects that keep the dictionary updated and relevant.
2. Spell Checking in Context:
• Allow for sentence structure and usage spell checking. The current tool can easily identify homophones through a dictionary lookup but may also provide suggestions according to context. This would greatly improve the accuracy of this tool.
3. User Interface Development:
•	Build an easy-to-use graphical interface for the spell-checker application so that more users can get to the application than would otherwise be unable to use command-line tools.
4. Integration with Other Tools:
 •	Determine how the spelling checker could be incorporated into common text editors and word processors, for instance, in order to run real-time spell checking as one types.
5. Multilingual Support:
• Spell Checking: Extend the tool with multilingual spell checking to allow users to conveniently switch between Dzongkha and other languages. This may involve adding other language dictionaries.
6. Improvements Using Machine Learning
• Use appropriate machine learning methods to improve error detection and correction. Herein, a model can be trained on a corpus of correctly spelled Dzongkha text for predicting and suggesting misspellings with corrections.
7. User Feedback Mechanism:
•	Provide a feedback mechanism wherein the user can report any dictionary entry that is incorrect or even add a new word. This will keep the dictionary updated and correct.
8.Performance Optimisation:
 •	Continuously evaluate and optimise spell checker performance to handle larger and more complicated files without sacrificing speed and efficiency.
9.Documentation and Tutorials:
•	Create full documentation and tutorials that will help users understand how they can work with the spell checker, examples, and best practices.
10. 10. Highlighting Errors:
•	Enhancing the output to highlight spelling errors through changing the color of the text or providing suggestions for corrections, making it easier for a user to locate and change the mistakes.

In this way, the Dzongkha Spell Checker can become full-featured, multi-functional, and allow a wider range of users while being adaptable to the emerging demands of the community of the Dzongkha language.

##Reference
1. Dzongkha Development Commission.  Dzongkha Language Resources.
2. youtube
3. chatgpt
4. github book

 

