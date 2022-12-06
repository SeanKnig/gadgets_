def GetAdapterHolder(numViews):
    storeArr = []
    initial = 1
    initial2 = 1
    imports = '''
        package com.example.asuandroid.vectorBuildAdapters;
        import android.annotation.SuppressLint;
        import android.content.Context;
        import android.media.Image;
        import android.view.LayoutInflater;
        import android.view.MenuItem;
        import android.view.ViewGroup;
        import android.widget.ImageView;
        import android.view.View;
        import android.widget.Toast;

        import com.example.asuandroid.R;
        import com.example.asuandroid.threads.MultithreadingDemo;

        import androidx.annotation.NonNull;
        import androidx.appcompat.widget.PopupMenu;
        import androidx.collection.ArraySet;
        import androidx.recyclerview.widget.RecyclerView;

        import java.util.ArrayList;
        import java.util.Arrays;
        import java.util.Collection;
        import java.util.Collections;
        import java.util.Comparator;
        import java.util.HashSet;
        import java.util.LinkedHashSet;
        import java.util.List;
        import java.util.Set;

        import static com.example.asuandroid.outfitfragments.Award2Fragment.context;

        import static com.example.asuandroid.outfitfragments.Award2Fragment.context;
        '''
    storeArr.append(imports)
    startEarly = '''
            public class RibbonAdapter%s extends RecyclerView.Adapter<RecyclerView.ViewHolder>{
                public static ArrayList<RibbonItem> mRibbonList;
                public static ArraySet<ImageView> images = new ArraySet<ImageView>();
                public static ArrayList<List<ImageView>> oaks = new ArrayList<>();
                public static List toPopup = new ArrayList<>();
                public static ArraySet<ImageView> currentOaks = new ArraySet<>();
                //private CompoundButton.OnCheckedChangeListener;
                private OnItemClickListener mListener;
                private static Context mContext = context;
            ''' %(numViews)
    storeArr.append(startEarly)
    for i in range(numViews):
        headerArr = "private final ArraySet<ImageView> oaks%s = new ArraySet<>();\n"%(i+1)
        startMid = "public static ImageView mImageView%s;\n"%(i+1)
        storeArr.append(headerArr)
        storeArr.append(startMid)
        for i in range(2,9):
            mid = "public static ImageView mImageView%s_%s;\n"%(initial, i)
            storeArr.append(mid)
        initial+=1
    inbetween = '''
        public ArrayList<RibbonItem> RibbonAdapter%s(ArrayList<RibbonItem> mRibbonList) {
        return mRibbonList;
    }
    public interface OnItemClickListener { void onEditRibbonClick(int ribbon, int position);}
    public void setOnItemClickListener(RibbonAdapter%s.OnItemClickListener listener) { mListener = listener; }
                '''%(numViews, numViews)
    start = '''
        public static class Ribbon%sHolder extends RecyclerView.ViewHolder {
        '''%(numViews)
    frfrMid = '''
            public Ribbon%sHolder(View itemView, OnItemClickListener listener, ArraySet<ImageView> images, ArrayList<List<ImageView>> oaks) {\n'''%(numViews)
    itsSoopah = "super(itemView);\n"
    storeArr.append(inbetween)
    storeArr.append(start)
    storeArr.append(frfrMid)
    storeArr.append(itsSoopah)
    for i in range(numViews):
        listy = "List<ImageView> oaks%s = new ArrayList<>();\n"%(i+1)
        shlisty = "mImageView%s = itemView.findViewById(R.id.ribbon%s);\n"%(i+1, i+1)
        thisty = "images.add(mImageView%s);\n"%(i+1)
        storeArr.append(listy)
        storeArr.append(shlisty)
        storeArr.append(thisty)
        for i in range(2,9):
            holyBuckets = "oaks%s.add(mImageView%s_%s = itemView.findViewById(R.id.ribbon%s_%s));\n"%(initial2, initial2, i, initial2, i)
            storeArr.append(holyBuckets)
        initial2 +=1
    for i in range(numViews):
        add = "oaks.add(oaks%s);\n"%(i+1)
        storeArr.append(add)
    for i in range(numViews):
        clickBUTTUHS = """
            RibbonAdapter%s.mImageView%s.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    showPopup(view, oaks, %s);
                }
            });
                """%(numViews, i+1, i)
        storeArr.append(clickBUTTUHS)
    haha = '''
            }
        }
        '''
    storeArr.append(haha) 
    adapter = '''
        public RibbonAdapter%s(ArrayList<RibbonItem> ribbonList) {
        mRibbonList = ribbonList;
    }'''%(numViews)
    storeArr.append(adapter)
    onBindSetup = '''
        @Override
        public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
            if (holder instanceof RibbonAdapter%s.Ribbon%sHolder) {
                RibbonItem currentItem = (RibbonItem) mRibbonList.get(position);''' %(numViews, numViews)
    storeArr.append(onBindSetup)
    for k in range(numViews):
        onBindIterate = '''mImageView%s.setImageResource(currentItem.getImageResource%s()); \n''' %(k+1, k+1)
        storeArr.append(onBindIterate)

    brackets = '''
        }
    }'''

    viewType = '''
        @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int ViewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.ribbon_item%s, parent, false);
        return new RibbonAdapter%s.Ribbon%sHolder(view, mListener, images, oaks);
    }
    '''%(numViews, numViews,numViews)
    rest = '''
        public static void showPopup(View v, ArrayList<List<ImageView>> oaks, int ribbonIndex){
        System.out.println();
        for(int i = 0; i < oaks.get(ribbonIndex).size() ; i++) {
            oaks.get(ribbonIndex).get(i).setImageResource(android.R.color.transparent);
        }
        System.out.println("oaks"+oaks);
        PopupMenu oakMenu = new PopupMenu(mContext, v);
        oakMenu.getMenuInflater().inflate(R.menu.oak_leaf_menu, oakMenu.getMenu());
        oakMenu.setOnMenuItemClickListener(new PopupMenu.OnMenuItemClickListener() {
            @Override
            public boolean onMenuItemClick(MenuItem item){
                switch (item.getItemId()) {
                    case R.id.item1:
                        Toast.makeText(context, "Item 1 clicked", Toast.LENGTH_SHORT).show();
                        oaks.get(ribbonIndex).get(0).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        return true;
                    case R.id.item2:
                        Toast.makeText(context, "Item 2 clicked", Toast.LENGTH_SHORT).show();
                        oaks.get(ribbonIndex).get(1).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(2).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        return true;
                    case R.id.item3:
                        Toast.makeText(context, "Item 3 clicked", Toast.LENGTH_SHORT).show();
                        oaks.get(ribbonIndex).get(0).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(3).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(4).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        return true;
                    case R.id.item4:
                        Toast.makeText(context, "Item 4 clicked", Toast.LENGTH_SHORT).show();
                        oaks.get(ribbonIndex).get(1).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(2).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(5).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        oaks.get(ribbonIndex).get(6).setImageResource(R.drawable.ic_bronze_oakleaf_3d);
                        return true;
                    default:
                        return false;
                }
            };
        });
        oakMenu.show();
    }
    @Override
    public int getItemViewType(int position) {
        RibbonItem currentItem = (RibbonItem) mRibbonList.get(position);
        if (currentItem instanceof RibbonItem.RibbonItem%s) {return %s;}
        return 0;
    }
    @Override
    public int getItemCount() {
        return mRibbonList.size();
    }
}
'''%(numViews, numViews)

    storeArr.append(brackets)
    storeArr.append(viewType)
    storeArr.append(rest)

    listToStrList = ' '.join([(elem) for elem in storeArr]) 
    print(listToStrList)
    file1 = open("this.txt","w")  
    file1.writelines(listToStrList)

GetAdapterHolder(49)
