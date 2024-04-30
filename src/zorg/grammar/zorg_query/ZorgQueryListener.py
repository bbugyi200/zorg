# Generated from src/zorg/grammar/zorg_query/ZorgQuery.g4 by ANTLR 4.13.1
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



del ZorgQueryParser