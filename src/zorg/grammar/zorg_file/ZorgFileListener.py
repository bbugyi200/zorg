# Generated from ZorgFile.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ZorgFileParser#body.
    def enterBody(self, ctx:ZorgFileParser.BodyContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#body.
    def exitBody(self, ctx:ZorgFileParser.BodyContext):
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


    # Enter a parse tree produced by ZorgFileParser#footnote.
    def enterFootnote(self, ctx:ZorgFileParser.FootnoteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#footnote.
    def exitFootnote(self, ctx:ZorgFileParser.FootnoteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#note.
    def enterNote(self, ctx:ZorgFileParser.NoteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#note.
    def exitNote(self, ctx:ZorgFileParser.NoteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#base_note.
    def enterBase_note(self, ctx:ZorgFileParser.Base_noteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#base_note.
    def exitBase_note(self, ctx:ZorgFileParser.Base_noteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#note_body.
    def enterNote_body(self, ctx:ZorgFileParser.Note_bodyContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#note_body.
    def exitNote_body(self, ctx:ZorgFileParser.Note_bodyContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#subnote.
    def enterSubnote(self, ctx:ZorgFileParser.SubnoteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#subnote.
    def exitSubnote(self, ctx:ZorgFileParser.SubnoteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#subsubnote.
    def enterSubsubnote(self, ctx:ZorgFileParser.SubsubnoteContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#subsubnote.
    def exitSubsubnote(self, ctx:ZorgFileParser.SubsubnoteContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#todo.
    def enterTodo(self, ctx:ZorgFileParser.TodoContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#todo.
    def exitTodo(self, ctx:ZorgFileParser.TodoContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#base_todo.
    def enterBase_todo(self, ctx:ZorgFileParser.Base_todoContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#base_todo.
    def exitBase_todo(self, ctx:ZorgFileParser.Base_todoContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#todo_prefix.
    def enterTodo_prefix(self, ctx:ZorgFileParser.Todo_prefixContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#todo_prefix.
    def exitTodo_prefix(self, ctx:ZorgFileParser.Todo_prefixContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#x_or_tilde.
    def enterX_or_tilde(self, ctx:ZorgFileParser.X_or_tildeContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#x_or_tilde.
    def exitX_or_tilde(self, ctx:ZorgFileParser.X_or_tildeContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#priority.
    def enterPriority(self, ctx:ZorgFileParser.PriorityContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#priority.
    def exitPriority(self, ctx:ZorgFileParser.PriorityContext):
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


    # Enter a parse tree produced by ZorgFileParser#atom.
    def enterAtom(self, ctx:ZorgFileParser.AtomContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#atom.
    def exitAtom(self, ctx:ZorgFileParser.AtomContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#zid.
    def enterZid(self, ctx:ZorgFileParser.ZidContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#zid.
    def exitZid(self, ctx:ZorgFileParser.ZidContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#property.
    def enterProperty(self, ctx:ZorgFileParser.PropertyContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#property.
    def exitProperty(self, ctx:ZorgFileParser.PropertyContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#simple_prop.
    def enterSimple_prop(self, ctx:ZorgFileParser.Simple_propContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#simple_prop.
    def exitSimple_prop(self, ctx:ZorgFileParser.Simple_propContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#inline_prop.
    def enterInline_prop(self, ctx:ZorgFileParser.Inline_propContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#inline_prop.
    def exitInline_prop(self, ctx:ZorgFileParser.Inline_propContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#id_group.
    def enterId_group(self, ctx:ZorgFileParser.Id_groupContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#id_group.
    def exitId_group(self, ctx:ZorgFileParser.Id_groupContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#id.
    def enterId(self, ctx:ZorgFileParser.IdContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#id.
    def exitId(self, ctx:ZorgFileParser.IdContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#date.
    def enterDate(self, ctx:ZorgFileParser.DateContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#date.
    def exitDate(self, ctx:ZorgFileParser.DateContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#time.
    def enterTime(self, ctx:ZorgFileParser.TimeContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#time.
    def exitTime(self, ctx:ZorgFileParser.TimeContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#any_symbol.
    def enterAny_symbol(self, ctx:ZorgFileParser.Any_symbolContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#any_symbol.
    def exitAny_symbol(self, ctx:ZorgFileParser.Any_symbolContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#non_tag_symbol.
    def enterNon_tag_symbol(self, ctx:ZorgFileParser.Non_tag_symbolContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#non_tag_symbol.
    def exitNon_tag_symbol(self, ctx:ZorgFileParser.Non_tag_symbolContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#id_symbol.
    def enterId_symbol(self, ctx:ZorgFileParser.Id_symbolContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#id_symbol.
    def exitId_symbol(self, ctx:ZorgFileParser.Id_symbolContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#tag_symbol.
    def enterTag_symbol(self, ctx:ZorgFileParser.Tag_symbolContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#tag_symbol.
    def exitTag_symbol(self, ctx:ZorgFileParser.Tag_symbolContext):
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


    # Enter a parse tree produced by ZorgFileParser#quoted.
    def enterQuoted(self, ctx:ZorgFileParser.QuotedContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#quoted.
    def exitQuoted(self, ctx:ZorgFileParser.QuotedContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#link.
    def enterLink(self, ctx:ZorgFileParser.LinkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#link.
    def exitLink(self, ctx:ZorgFileParser.LinkContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#global_link.
    def enterGlobal_link(self, ctx:ZorgFileParser.Global_linkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#global_link.
    def exitGlobal_link(self, ctx:ZorgFileParser.Global_linkContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#local_link.
    def enterLocal_link(self, ctx:ZorgFileParser.Local_linkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#local_link.
    def exitLocal_link(self, ctx:ZorgFileParser.Local_linkContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#zid_link.
    def enterZid_link(self, ctx:ZorgFileParser.Zid_linkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#zid_link.
    def exitZid_link(self, ctx:ZorgFileParser.Zid_linkContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#embedded_link.
    def enterEmbedded_link(self, ctx:ZorgFileParser.Embedded_linkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#embedded_link.
    def exitEmbedded_link(self, ctx:ZorgFileParser.Embedded_linkContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#ref.
    def enterRef(self, ctx:ZorgFileParser.RefContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#ref.
    def exitRef(self, ctx:ZorgFileParser.RefContext):
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


    # Enter a parse tree produced by ZorgFileParser#eol.
    def enterEol(self, ctx:ZorgFileParser.EolContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#eol.
    def exitEol(self, ctx:ZorgFileParser.EolContext):
        pass



del ZorgFileParser