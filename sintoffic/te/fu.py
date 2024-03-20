def click_ID(driver, time, id):
    """Clicks on element by it's ID.

    Args:
        driver: WebDriver instance.
        time: Time to wait for element to be clickable.
        id: ID of the element to click.
    """

    try:
        WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.ID, id))
        ).click()
        print(f"Clicked on element with ID: {id}")
    except TimeoutException:
        print(f"Could not click on element with ID: {id}")
        raise

