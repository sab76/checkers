#include "StudentAI.h"
#include <random>

//The following part should be completed by students.
//The students can modify anything except the class name and exisiting functions and varibles.
StudentAI::StudentAI(int col,int row,int p)
	:AI(col, row, p)
{
    board = Board(col,row,p);
    board.initializeGame();
    player = 2;
}

int StudentAI::countCaptures(const Move& move) {
    int captureCount = 0;
    for (int i = 0; i < move.seq.size() - 1; ++i) {
        if (abs(move.seq[i][0] - move.seq[i + 1][0]) > 1 && abs(move.seq[i][1] - move.seq[i + 1][1]) > 1) {
            captureCount++;
        }
    }
    return captureCount;
}

Move StudentAI::GetMove(Move move)
{
    if (move.seq.empty())
    {
        player = 1;
    } else{
        board.makeMove(move,player == 1?2:1);
    }
    vector<vector<Move> > moves = board.getAllPossibleMoves(player);

    Move bestMove;
    int maxCaptures = 0;

    for (const auto& checker_moves : moves) {
        for (const auto& m : checker_moves) {
            if (m.isCapture()) {
                int captureCount = countCaptures(m);
                if (captureCount > maxCaptures) {
                    maxCaptures = captureCount;
                    bestMove = m;
                }
            }
        }
    }

    if (maxCaptures > 0) {
        board.makeMove(bestMove, player);
        return bestMove;
    }

    int i = rand() % (moves.size());
    vector<Move> checker_moves = moves[i];
    int j = rand() % (checker_moves.size());
    Move res = checker_moves[j];
    board.makeMove(res,player);
    return res;
}

