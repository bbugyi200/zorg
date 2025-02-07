# Generated from ZorgFile.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by ZorgFileParser#word_group.
    def enterWord_group(self, ctx:ZorgFileParser.Word_groupContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#word_group.
    def exitWord_group(self, ctx:ZorgFileParser.Word_groupContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#before_word.
    def enterBefore_word(self, ctx:ZorgFileParser.Before_wordContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#before_word.
    def exitBefore_word(self, ctx:ZorgFileParser.Before_wordContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#word.
    def enterWord(self, ctx:ZorgFileParser.WordContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#word.
    def exitWord(self, ctx:ZorgFileParser.WordContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#after_word.
    def enterAfter_word(self, ctx:ZorgFileParser.After_wordContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#after_word.
    def exitAfter_word(self, ctx:ZorgFileParser.After_wordContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#unquoted_word.
    def enterUnquoted_word(self, ctx:ZorgFileParser.Unquoted_wordContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#unquoted_word.
    def exitUnquoted_word(self, ctx:ZorgFileParser.Unquoted_wordContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#quoted_word.
    def enterQuoted_word(self, ctx:ZorgFileParser.Quoted_wordContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#quoted_word.
    def exitQuoted_word(self, ctx:ZorgFileParser.Quoted_wordContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#quoted_word_body.
    def enterQuoted_word_body(self, ctx:ZorgFileParser.Quoted_word_bodyContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#quoted_word_body.
    def exitQuoted_word_body(self, ctx:ZorgFileParser.Quoted_word_bodyContext):
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


    # Enter a parse tree produced by ZorgFileParser#simple_prop_value.
    def enterSimple_prop_value(self, ctx:ZorgFileParser.Simple_prop_valueContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#simple_prop_value.
    def exitSimple_prop_value(self, ctx:ZorgFileParser.Simple_prop_valueContext):
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


    # Enter a parse tree produced by ZorgFileParser#priv_id.
    def enterPriv_id(self, ctx:ZorgFileParser.Priv_idContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#priv_id.
    def exitPriv_id(self, ctx:ZorgFileParser.Priv_idContext):
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


    # Enter a parse tree produced by ZorgFileParser#any_sym.
    def enterAny_sym(self, ctx:ZorgFileParser.Any_symContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#any_sym.
    def exitAny_sym(self, ctx:ZorgFileParser.Any_symContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#non_tag_sym.
    def enterNon_tag_sym(self, ctx:ZorgFileParser.Non_tag_symContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#non_tag_sym.
    def exitNon_tag_sym(self, ctx:ZorgFileParser.Non_tag_symContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#id_sym.
    def enterId_sym(self, ctx:ZorgFileParser.Id_symContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#id_sym.
    def exitId_sym(self, ctx:ZorgFileParser.Id_symContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#tag_sym.
    def enterTag_sym(self, ctx:ZorgFileParser.Tag_symContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#tag_sym.
    def exitTag_sym(self, ctx:ZorgFileParser.Tag_symContext):
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


    # Enter a parse tree produced by ZorgFileParser#ref_link.
    def enterRef_link(self, ctx:ZorgFileParser.Ref_linkContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#ref_link.
    def exitRef_link(self, ctx:ZorgFileParser.Ref_linkContext):
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


    # Enter a parse tree produced by ZorgFileParser#url.
    def enterUrl(self, ctx:ZorgFileParser.UrlContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url.
    def exitUrl(self, ctx:ZorgFileParser.UrlContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_schema.
    def enterUrl_schema(self, ctx:ZorgFileParser.Url_schemaContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_schema.
    def exitUrl_schema(self, ctx:ZorgFileParser.Url_schemaContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_domain.
    def enterUrl_domain(self, ctx:ZorgFileParser.Url_domainContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_domain.
    def exitUrl_domain(self, ctx:ZorgFileParser.Url_domainContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_port.
    def enterUrl_port(self, ctx:ZorgFileParser.Url_portContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_port.
    def exitUrl_port(self, ctx:ZorgFileParser.Url_portContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_path.
    def enterUrl_path(self, ctx:ZorgFileParser.Url_pathContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_path.
    def exitUrl_path(self, ctx:ZorgFileParser.Url_pathContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_path_part.
    def enterUrl_path_part(self, ctx:ZorgFileParser.Url_path_partContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_path_part.
    def exitUrl_path_part(self, ctx:ZorgFileParser.Url_path_partContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_query.
    def enterUrl_query(self, ctx:ZorgFileParser.Url_queryContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_query.
    def exitUrl_query(self, ctx:ZorgFileParser.Url_queryContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_key_val.
    def enterUrl_key_val(self, ctx:ZorgFileParser.Url_key_valContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_key_val.
    def exitUrl_key_val(self, ctx:ZorgFileParser.Url_key_valContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_fragment.
    def enterUrl_fragment(self, ctx:ZorgFileParser.Url_fragmentContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_fragment.
    def exitUrl_fragment(self, ctx:ZorgFileParser.Url_fragmentContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#url_atom.
    def enterUrl_atom(self, ctx:ZorgFileParser.Url_atomContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#url_atom.
    def exitUrl_atom(self, ctx:ZorgFileParser.Url_atomContext):
        pass


    # Enter a parse tree produced by ZorgFileParser#https.
    def enterHttps(self, ctx:ZorgFileParser.HttpsContext):
        pass

    # Exit a parse tree produced by ZorgFileParser#https.
    def exitHttps(self, ctx:ZorgFileParser.HttpsContext):
        pass



del ZorgFileParser