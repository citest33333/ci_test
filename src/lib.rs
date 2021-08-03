use std::ops::Add;

#[cfg(test)]
mod tests {
    use super::add;

    #[test]
    fn add_two_and_one() {
        assert_eq!(add(2, 1), 3);
    }

    #[test]
    fn add_two_and_two() {
        assert_eq!(add(2, 2), 4);
    }
}

#[allow(dead_code)]
fn add<T>(a: T, b: T) -> T
where
    T: Add<Output = T>,
{
    a + b
}
