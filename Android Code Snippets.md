##
**Author :** Akshay Chavan
##

**Comma Separated Numbers:**

String.format("%,d", NumberFormat.getNumberInstance(Locale.US).parse(yourNumberString.trim()))
________________________________________________________________________________________________________

**Gradient Line:** 

Drawable-

<?xml version="1.0" encoding="utf-8"?>
< shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle"
    >
    < gradient
        android:endColor="@android:color/transparent"
        android:centerColor="@color/text_color"
        android:startColor="@android:color/transparent"
        android:angle="0"
        android:type="linear"/>
< /shape>

XML-

< ImageView
                android:id="@+id/hr"
                android:layout_width="match_parent"
                android:layout_height="1dp"
                android:background="@drawable/gradient_line"
                android:gravity="center_horizontal"
                />

________________________________________________________________________________________________________

**Custom Arraylist Sorting:**

Collections.sort(sharesList, new Comparator<yourArrayListType>() {
                            @Override
                            public int compare(yourArrayListType item1, yourArrayListType item2) {
                                String s1 = item1.getfieldName();
                                String s2 = item2.getfieldName();
                                return s1.compareToIgnoreCase(s2);
                            }
});
________________________________________________________________________________________________________





**Textview with Marquee effect:**

 < TextView android:layout_width="wrap_content"
                            android:layout_height="0dp"
                            android:fadingEdge="horizontal"
                            android:singleLine="true"
                            android:ellipsize="marquee"
                            android:marqueeRepeatLimit="marquee_forever"
                            android:padding="@dimen/text_inner_padding"
                            android:scrollHorizontally="true"
                            android:textSize="13dp" />

________________________________________________________________________________________________________

**Horizontal Line:**

< View
                    android:layout_width="match_parent"
                    android:layout_height="1dp"
                    android:layout_marginTop="10dp"
                    android:background="#494949" />

________________________________________________________________________________________________________

**Vertical Line:**

< View
                        android:layout_width="0dp"
                        android:layout_height="100dp"
                        android:layout_gravity="center"
                        android:layout_weight="0.01"
                        android:background="#494949" />

________________________________________________________________________________________________________

**Decimal Points Formatting for Number:**

String.format("%.4f", val);

________________________________________________________________________________________________________

Decimal Points Formatting for an Input Field:

@Override
            public void afterTextChanged(Editable s) {
                if (s.toString().length() != 0) {
                    et_ko_percentage.removeTextChangedListener(this);

                    int integerPlaces = s.toString().indexOf('.');          // 122.58 => 3
                    int decimalPlaces = s.toString().length() - integerPlaces - 1;      // 6 - 3 - 1
                    // Log.e(TAG,"Integer Places: "+integerPlaces+" Decimal Places: "+decimalPlaces);
                    float koPerc = Float.parseFloat(s.toString());
                    //if (Float.parseFloat(String.format("%.2f", koPerc)) != koPerc)
                    if (s.toString().contains(".") && decimalPlaces > 2) {
                        et_ko_percentage.setText(String.format("%.2f", koPerc));
                    }
                    et_ko_percentage.setSelection(et_ko_percentage.getText().length());
                    et_ko_percentage.addTextChangedListener(this);
                }
            }
________________________________________________________________________________________________________

**Input field value formatting:**

et_popup_notional.addTextChangedListener(new TextWatcher() {
                    @Override
                    public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                    }

                    @Override
                    public void onTextChanged(CharSequence s, int start, int before, int count) {

                    }

                    @Override
                    public void afterTextChanged(Editable s) {

                        // number formatting for nominal amount

                        Number nominal = null;
                        try {
                            // The comma in the format specifier does the trick
                            nominal = NumberFormat.getNumberInstance(java.util.Locale.US).parse(s.toString().trim());
                            Log.e(TAG, "Nominal->" + nominal);
                        } catch (NumberFormatException | ParseException e) {
                        }
                        // Set s back to the view after temporarily removing the text change listener
                        et_popup_notional.removeTextChangedListener(this);
                        et_popup_notional.setText(String.format("%,d", nominal));
                        et_popup_notional.setSelection(et_popup_notional.getText().length());
                        et_popup_notional.addTextChangedListener(this);
                    }
                });
________________________________________________________________________________________________________
**API Calls Optimization:**

public void saveArrayList(ArrayList<ShareListPojo> sharesList) {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(AveragingAutocall.this);
        SharedPreferences.Editor editor = prefs.edit();
        Gson gson = new Gson();
        String json = gson.toJson(sharesList);
        editor.putString("SHARES_LIST_LOADED", json);
        editor.apply();

        MySingletonClass.getInstance().setSharesLoadedFlag(true);

    }       // end writeJsonToLocal


    public ArrayList<ShareListPojo> getArrayList() {
        Toast.makeText(this, "Loading previous shares list", Toast.LENGTH_SHORT).show();

        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(AveragingAutocall.this);
        Gson gson = new Gson();
        String json = prefs.getString("SHARES_LIST_LOADED", null);
        Type listType = new TypeToken<ArrayList<ShareListPojo>>() {
        }.getType();
        // ArrayList<ShareListPojo> mSomeArraylist = gson.fromJson(json, listType);
        return gson.fromJson(json, listType);
        //Toast.makeText(this, "Test->"+mSomeArraylist.get(0).getLongName(),Toast.LENGTH_SHORT).show();
    }       // end getArrayList()

________________________________________________________________________________________________________

**Synchronous Retrofit Call:**

try {
                    // ------------------- CurrentVal_PortfolioRequest -------------------------
                    EQGetWatchListDataAPIRequest.put("WatchListName", this.watchlistName);            // Default -> "Watchlist1"
                    EQGetWatchListDataAPIRequest.put("CustomerID", "32768");
                    EQGetWatchListDataAPIRequest.put("EntityID", "4");
                    EQGetWatchListDataAPIRequest.put("LoginID", "Dealer1");

                    // ------------------- mainObj -------------------------
                    mainObj.put("FinIQRequestHeader", FinIQRequestHeader);
                    mainObj.put("EQGetWatchListDataAPIRequest", EQGetWatchListDataAPIRequest);

                    Log.e(TAG, "Get Watchlist Product Data Shares API Input parameters -> " + mainObj.toString());

                    ApiInterface apiInterface = ApiClient.getClient().create(ApiInterface.class);

                    Call<GetWatchlistDataSharesPojo> call = apiInterface.getWatchlistDataShares(mainObj.toString());

                    // ----------------------------------- Synchronous Call ---------------------------------------------
                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);

                    Response<GetWatchlistDataSharesPojo> response = call.execute();
                    GetWatchlistDataSharesPojo getWatchlistDataSharesPojo = response.body();
                    for (GetWatchlistDataResponseItem item : getWatchlistDataSharesPojo.getEQGetWatchListDataAPIResponse().getItems()) {
                        callGetProductInfoSharesAPI(item.getNoteMasterId());
                    }

                } catch (IOException | JSONException e) {
                    Toast.makeText(getContext(), "TRY CATCH ERROR!\n>>" + e.getMessage(), Toast.LENGTH_SHORT).show();
                }
