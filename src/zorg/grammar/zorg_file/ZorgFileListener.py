# Generated from src/zorg/grammar/zorg_file/ZorgFile.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZorgFileParser import ZorgFileParser
else:
    from ZorgFileParser import ZorgFileParser

# This class defines a complete listener for a parse tree produced by ZorgFileParser.
class ZorgFileListener(ParseTreeListener):

    # Enter a parse tree produced by ZorgFileParser#prog.
    def enterProg(self, ctx:ZorgFileParser.ProgContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#prog.
    def exitProg(self, ctx:ZorgFileParser.ProgContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#head.
    def enterHead(self, ctx:ZorgFileParser.HeadContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#head.
    def exitHead(self, ctx:ZorgFileParser.HeadContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#comment.
    def enterComment(self, ctx:ZorgFileParser.CommentContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#comment.
    def exitComment(self, ctx:ZorgFileParser.CommentContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#block.
    def enterBlock(self, ctx:ZorgFileParser.BlockContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#block.
    def exitBlock(self, ctx:ZorgFileParser.BlockContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#item.
    def enterItem(self, ctx:ZorgFileParser.ItemContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#item.
    def exitItem(self, ctx:ZorgFileParser.ItemContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#todo.
    def enterTodo(self, ctx:ZorgFileParser.TodoContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#todo.
    def exitTodo(self, ctx:ZorgFileParser.TodoContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#priority.
    def enterPriority(self, ctx:ZorgFileParser.PriorityContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#priority.
    def exitPriority(self, ctx:ZorgFileParser.PriorityContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#note.
    def enterNote(self, ctx:ZorgFileParser.NoteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#note.
    def exitNote(self, ctx:ZorgFileParser.NoteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#space_atoms.
    def enterSpace_atoms(self, ctx:ZorgFileParser.Space_atomsContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#space_atoms.
    def exitSpace_atoms(self, ctx:ZorgFileParser.Space_atomsContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#space_atom.
    def enterSpace_atom(self, ctx:ZorgFileParser.Space_atomContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#space_atom.
    def exitSpace_atom(self, ctx:ZorgFileParser.Space_atomContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#property.
    def enterProperty(self, ctx:ZorgFileParser.PropertyContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#property.
    def exitProperty(self, ctx:ZorgFileParser.PropertyContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#tag.
    def enterTag(self, ctx:ZorgFileParser.TagContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#tag.
    def exitTag(self, ctx:ZorgFileParser.TagContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#area.
    def enterArea(self, ctx:ZorgFileParser.AreaContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#area.
    def exitArea(self, ctx:ZorgFileParser.AreaContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#context.
    def enterContext(self, ctx:ZorgFileParser.ContextContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#context.
    def exitContext(self, ctx:ZorgFileParser.ContextContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#person.
    def enterPerson(self, ctx:ZorgFileParser.PersonContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#person.
    def exitPerson(self, ctx:ZorgFileParser.PersonContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#project.
    def enterProject(self, ctx:ZorgFileParser.ProjectContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#project.
    def exitProject(self, ctx:ZorgFileParser.ProjectContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h1_section.
    def enterH1_section(self, ctx:ZorgFileParser.H1_sectionContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h1_section.
    def exitH1_section(self, ctx:ZorgFileParser.H1_sectionContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h2_section.
    def enterH2_section(self, ctx:ZorgFileParser.H2_sectionContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h2_section.
    def exitH2_section(self, ctx:ZorgFileParser.H2_sectionContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h3_section.
    def enterH3_section(self, ctx:ZorgFileParser.H3_sectionContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h3_section.
    def exitH3_section(self, ctx:ZorgFileParser.H3_sectionContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h4_section.
    def enterH4_section(self, ctx:ZorgFileParser.H4_sectionContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h4_section.
    def exitH4_section(self, ctx:ZorgFileParser.H4_sectionContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h1_header.
    def enterH1_header(self, ctx:ZorgFileParser.H1_headerContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h1_header.
    def exitH1_header(self, ctx:ZorgFileParser.H1_headerContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h2_header.
    def enterH2_header(self, ctx:ZorgFileParser.H2_headerContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h2_header.
    def exitH2_header(self, ctx:ZorgFileParser.H2_headerContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h3_header.
    def enterH3_header(self, ctx:ZorgFileParser.H3_headerContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h3_header.
    def exitH3_header(self, ctx:ZorgFileParser.H3_headerContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#h4_header.
    def enterH4_header(self, ctx:ZorgFileParser.H4_headerContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#h4_header.
    def exitH4_header(self, ctx:ZorgFileParser.H4_headerContext):
        pass



del ZorgFileParser