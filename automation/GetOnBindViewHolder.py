def GetRandomHolder(numViews):
    storeArr = []
    start = '''
            case %s:
                RibbonAdapter%s mAdapter%s = new RibbonAdapter%s(mRibbonList);
                mRecyclerViewAdapter%s = new RibbonAdapter%s(mRibbonList);
                final RecyclerView recyclerView%s = view.findViewById(R.id.recyclerViewRibbonRack);
                LinearLayoutManager layoutManager%s = new LinearLayoutManager(c);
                recyclerView%s.setLayoutManager(layoutManager%s);
                recyclerView%s.setAdapter(mAdapter%s);
                break;'''%(numViews,numViews,numViews,numViews,numViews,numViews,numViews,numViews,numViews,numViews,numViews,numViews)

    print(start)
    #end = '''private RibbonAdapter%s mRecyclerViewAdapter%s;'''%(numViews, numViews)
    #print(end)
for i in range(51):
    GetRandomHolder(i)
