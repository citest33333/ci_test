use std::ops::Add;

#[cfg(test)]
mod tests {
    use super::add;

    #[test]
    fn it_works() {
        assert_eq!(add(2, 1), 3);
    }
}

#[allow(dead_code)]
fn add<T>(a: T, b: T) -> T
where
    T: Add<Output = T>,
{
    a + b
}
