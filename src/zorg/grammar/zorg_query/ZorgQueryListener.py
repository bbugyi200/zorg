# Generated from ZorgQuery.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZorgQueryParser import ZorgQueryParser
else:
    from ZorgQueryParser import ZorgQueryParser

# This class defines a complete listener for a parse tree produced by ZorgQueryParser.
class ZorgQueryListener(ParseTreeListener):

    # Enter a parse tree produced by ZorgQueryParser#prog.
    def enterProg(self, ctx:ZorgQueryParser.ProgContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#prog.
    def exitProg(self, ctx:ZorgQueryParser.ProgContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#query.
    def enterQuery(self, ctx:ZorgQueryParser.QueryContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#query.
    def exitQuery(self, ctx:ZorgQueryParser.QueryContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#where_query.
    def enterWhere_query(self, ctx:ZorgQueryParser.Where_queryContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#where_query.
    def exitWhere_query(self, ctx:ZorgQueryParser.Where_queryContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#select_query.
    def enterSelect_query(self, ctx:ZorgQueryParser.Select_queryContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#select_query.
    def exitSelect_query(self, ctx:ZorgQueryParser.Select_queryContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#select.
    def enterSelect(self, ctx:ZorgQueryParser.SelectContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#select.
    def exitSelect(self, ctx:ZorgQueryParser.SelectContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#where.
    def enterWhere(self, ctx:ZorgQueryParser.WhereContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#where.
    def exitWhere(self, ctx:ZorgQueryParser.WhereContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#order_by.
    def enterOrder_by(self, ctx:ZorgQueryParser.Order_byContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#order_by.
    def exitOrder_by(self, ctx:ZorgQueryParser.Order_byContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#group_by.
    def enterGroup_by(self, ctx:ZorgQueryParser.Group_byContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#group_by.
    def exitGroup_by(self, ctx:ZorgQueryParser.Group_byContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#select_body.
    def enterSelect_body(self, ctx:ZorgQueryParser.Select_bodyContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#select_body.
    def exitSelect_body(self, ctx:ZorgQueryParser.Select_bodyContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#note.
    def enterNote(self, ctx:ZorgQueryParser.NoteContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#note.
    def exitNote(self, ctx:ZorgQueryParser.NoteContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#where_body.
    def enterWhere_body(self, ctx:ZorgQueryParser.Where_bodyContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#where_body.
    def exitWhere_body(self, ctx:ZorgQueryParser.Where_bodyContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#or_filter.
    def enterOr_filter(self, ctx:ZorgQueryParser.Or_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#or_filter.
    def exitOr_filter(self, ctx:ZorgQueryParser.Or_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#and_filter.
    def enterAnd_filter(self, ctx:ZorgQueryParser.And_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#and_filter.
    def exitAnd_filter(self, ctx:ZorgQueryParser.And_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#where_atom.
    def enterWhere_atom(self, ctx:ZorgQueryParser.Where_atomContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#where_atom.
    def exitWhere_atom(self, ctx:ZorgQueryParser.Where_atomContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#note_type.
    def enterNote_type(self, ctx:ZorgQueryParser.Note_typeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#note_type.
    def exitNote_type(self, ctx:ZorgQueryParser.Note_typeContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#note_type_char.
    def enterNote_type_char(self, ctx:ZorgQueryParser.Note_type_charContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#note_type_char.
    def exitNote_type_char(self, ctx:ZorgQueryParser.Note_type_charContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#priority_range.
    def enterPriority_range(self, ctx:ZorgQueryParser.Priority_rangeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#priority_range.
    def exitPriority_range(self, ctx:ZorgQueryParser.Priority_rangeContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#tag.
    def enterTag(self, ctx:ZorgQueryParser.TagContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#tag.
    def exitTag(self, ctx:ZorgQueryParser.TagContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#not_op.
    def enterNot_op(self, ctx:ZorgQueryParser.Not_opContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#not_op.
    def exitNot_op(self, ctx:ZorgQueryParser.Not_opContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#area.
    def enterArea(self, ctx:ZorgQueryParser.AreaContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#area.
    def exitArea(self, ctx:ZorgQueryParser.AreaContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#context.
    def enterContext(self, ctx:ZorgQueryParser.ContextContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#context.
    def exitContext(self, ctx:ZorgQueryParser.ContextContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#person.
    def enterPerson(self, ctx:ZorgQueryParser.PersonContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#person.
    def exitPerson(self, ctx:ZorgQueryParser.PersonContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#project.
    def enterProject(self, ctx:ZorgQueryParser.ProjectContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#project.
    def exitProject(self, ctx:ZorgQueryParser.ProjectContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#subfilter.
    def enterSubfilter(self, ctx:ZorgQueryParser.SubfilterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#subfilter.
    def exitSubfilter(self, ctx:ZorgQueryParser.SubfilterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#create_range.
    def enterCreate_range(self, ctx:ZorgQueryParser.Create_rangeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#create_range.
    def exitCreate_range(self, ctx:ZorgQueryParser.Create_rangeContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#modify_range.
    def enterModify_range(self, ctx:ZorgQueryParser.Modify_rangeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#modify_range.
    def exitModify_range(self, ctx:ZorgQueryParser.Modify_rangeContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#prop_filter.
    def enterProp_filter(self, ctx:ZorgQueryParser.Prop_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#prop_filter.
    def exitProp_filter(self, ctx:ZorgQueryParser.Prop_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#prop_op.
    def enterProp_op(self, ctx:ZorgQueryParser.Prop_opContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#prop_op.
    def exitProp_op(self, ctx:ZorgQueryParser.Prop_opContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#desc_filter.
    def enterDesc_filter(self, ctx:ZorgQueryParser.Desc_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#desc_filter.
    def exitDesc_filter(self, ctx:ZorgQueryParser.Desc_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#s_desc_filter.
    def enterS_desc_filter(self, ctx:ZorgQueryParser.S_desc_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#s_desc_filter.
    def exitS_desc_filter(self, ctx:ZorgQueryParser.S_desc_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#d_desc_filter.
    def enterD_desc_filter(self, ctx:ZorgQueryParser.D_desc_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#d_desc_filter.
    def exitD_desc_filter(self, ctx:ZorgQueryParser.D_desc_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#file_filter.
    def enterFile_filter(self, ctx:ZorgQueryParser.File_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#file_filter.
    def exitFile_filter(self, ctx:ZorgQueryParser.File_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#link_filter.
    def enterLink_filter(self, ctx:ZorgQueryParser.Link_filterContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#link_filter.
    def exitLink_filter(self, ctx:ZorgQueryParser.Link_filterContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#zid.
    def enterZid(self, ctx:ZorgQueryParser.ZidContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#zid.
    def exitZid(self, ctx:ZorgQueryParser.ZidContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#id.
    def enterId(self, ctx:ZorgQueryParser.IdContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#id.
    def exitId(self, ctx:ZorgQueryParser.IdContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#date.
    def enterDate(self, ctx:ZorgQueryParser.DateContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#date.
    def exitDate(self, ctx:ZorgQueryParser.DateContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#time.
    def enterTime(self, ctx:ZorgQueryParser.TimeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#time.
    def exitTime(self, ctx:ZorgQueryParser.TimeContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#any_non_squote.
    def enterAny_non_squote(self, ctx:ZorgQueryParser.Any_non_squoteContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#any_non_squote.
    def exitAny_non_squote(self, ctx:ZorgQueryParser.Any_non_squoteContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#any_non_dquote.
    def enterAny_non_dquote(self, ctx:ZorgQueryParser.Any_non_dquoteContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#any_non_dquote.
    def exitAny_non_dquote(self, ctx:ZorgQueryParser.Any_non_dquoteContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#desc_symbol.
    def enterDesc_symbol(self, ctx:ZorgQueryParser.Desc_symbolContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#desc_symbol.
    def exitDesc_symbol(self, ctx:ZorgQueryParser.Desc_symbolContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#non_tag_symbol.
    def enterNon_tag_symbol(self, ctx:ZorgQueryParser.Non_tag_symbolContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#non_tag_symbol.
    def exitNon_tag_symbol(self, ctx:ZorgQueryParser.Non_tag_symbolContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#id_symbol.
    def enterId_symbol(self, ctx:ZorgQueryParser.Id_symbolContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#id_symbol.
    def exitId_symbol(self, ctx:ZorgQueryParser.Id_symbolContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#tag_symbol.
    def enterTag_symbol(self, ctx:ZorgQueryParser.Tag_symbolContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#tag_symbol.
    def exitTag_symbol(self, ctx:ZorgQueryParser.Tag_symbolContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#group_by_body.
    def enterGroup_by_body(self, ctx:ZorgQueryParser.Group_by_bodyContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#group_by_body.
    def exitGroup_by_body(self, ctx:ZorgQueryParser.Group_by_bodyContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#group_by_atom.
    def enterGroup_by_atom(self, ctx:ZorgQueryParser.Group_by_atomContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#group_by_atom.
    def exitGroup_by_atom(self, ctx:ZorgQueryParser.Group_by_atomContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#order_by_body.
    def enterOrder_by_body(self, ctx:ZorgQueryParser.Order_by_bodyContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#order_by_body.
    def exitOrder_by_body(self, ctx:ZorgQueryParser.Order_by_bodyContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#order_by_atom.
    def enterOrder_by_atom(self, ctx:ZorgQueryParser.Order_by_atomContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#order_by_atom.
    def exitOrder_by_atom(self, ctx:ZorgQueryParser.Order_by_atomContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#create.
    def enterCreate(self, ctx:ZorgQueryParser.CreateContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#create.
    def exitCreate(self, ctx:ZorgQueryParser.CreateContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#modify.
    def enterModify(self, ctx:ZorgQueryParser.ModifyContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#modify.
    def exitModify(self, ctx:ZorgQueryParser.ModifyContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#priority.
    def enterPriority(self, ctx:ZorgQueryParser.PriorityContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#priority.
    def exitPriority(self, ctx:ZorgQueryParser.PriorityContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#file.
    def enterFile(self, ctx:ZorgQueryParser.FileContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#file.
    def exitFile(self, ctx:ZorgQueryParser.FileContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#type.
    def enterType(self, ctx:ZorgQueryParser.TypeContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#type.
    def exitType(self, ctx:ZorgQueryParser.TypeContext):
        pass



del ZorgQueryParser