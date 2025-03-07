export const formatNumber = (num: number) => {
    // very handy function for this
    let formatter = Intl.NumberFormat('en', {notation: 'compact', maximumFractionDigits: 2});
    return formatter.format(num);
};

