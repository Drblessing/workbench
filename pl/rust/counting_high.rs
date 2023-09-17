fn main() {
    let mut counter: u128 = 0;
    while counter < 1_000_000_000 {
        counter += 1;
    }
    println!("{}", counter);
}
