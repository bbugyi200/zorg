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


    # Enter a parse tree produced by ZorgQueryParser#note_status.
    def enterNote_status(self, ctx:ZorgQueryParser.Note_statusContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#note_status.
    def exitNote_status(self, ctx:ZorgQueryParser.Note_statusContext):
        pass


    # Enter a parse tree produced by ZorgQueryParser#note_status_char.
    def enterNote_status_char(self, ctx:ZorgQueryParser.Note_status_charContext):
        pass

    # Exit a parse tree produced by ZorgQueryParser#note_status_char.
    def exitNote_status_char(self, ctx:ZorgQueryParser.Note_status_charContext):
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



del ZorgQueryParser